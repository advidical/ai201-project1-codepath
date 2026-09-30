"""
bm25.py — a small, dependency-free BM25 index, plus Reciprocal Rank Fusion
(RRF) to combine BM25's ranking with your existing semantic-search ranking.

Why RRF and not "just average the scores": BM25 scores and cosine-distance
scores live on completely different, uncalibrated scales (BM25 is an
unbounded positive score where higher is better; your `distance` is
0.0-ish to ~1.0+ where LOWER is better). Averaging them directly means
whichever one happens to have a bigger numeric range silently dominates.
RRF sidesteps that by only ever looking at *rank position* (1st, 2nd, 3rd...)
from each method, never the raw score — so the two methods are always on
equal footing. This is the standard, low-effort way to fuse rankings; see
Cormack, Clarke & Buettcher, "Reciprocal Rank Fusion outperforms Condorcet
and Individual Rank Learning Methods", SIGIR 2009:
https://plg.uwaterloo.ca/~gvcormac/cormacksigir09-rrf.pdf
"""

import math
import re
from collections import Counter

_TOKEN = re.compile(r"[a-z0-9]+")

# Standard English stopwords (the same set nltk's `stopwords.words("english")`
# ships, adjusted for the fact that our tokenizer strips apostrophes before
# this ever runs — so "don't" tokenizes to "don" + "t", "you're" to "you" +
# "re", etc., and those split-apart pieces need to be in the set too, not
# just the original contraction).
STOPWORDS = frozenset({
    "i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your",
    "yours", "yourself", "yourselves", "he", "him", "his", "himself", "she",
    "her", "hers", "herself", "it", "its", "itself", "they", "them", "their",
    "theirs", "themselves", "what", "which", "who", "whom", "this", "that",
    "these", "those", "am", "is", "are", "was", "were", "be", "been", "being",
    "have", "has", "had", "having", "do", "does", "did", "doing", "a", "an",
    "the", "and", "but", "if", "or", "because", "as", "until", "while", "of",
    "at", "by", "for", "with", "about", "against", "between", "into",
    "through", "during", "before", "after", "above", "below", "to", "from",
    "up", "down", "in", "out", "on", "off", "over", "under", "again",
    "further", "then", "once", "here", "there", "when", "where", "why", "how",
    "all", "any", "both", "each", "few", "more", "most", "other", "some",
    "such", "no", "nor", "not", "only", "own", "same", "so", "than", "too",
    "very", "s", "t", "can", "will", "just", "don", "should", "now", "d",
    "ll", "m", "o", "re", "ve", "y", "ain", "aren", "couldn", "didn", "doesn",
    "hadn", "hasn", "haven", "isn", "ma", "mightn", "mustn", "needn", "shan",
    "shouldn", "wasn", "weren", "won", "wouldn",
})


def _tokenize(text: str) -> list[str]:
    return [t for t in _TOKEN.findall(text.lower()) if t not in STOPWORDS]


class BM25Index:
    """
    Okapi BM25 over a fixed corpus of documents (your chunks).

    Build once per corpus with `BM25Index(chunk_texts)`, then call
    `.rank(query)` per question to get chunk indices sorted best-first.

    k1 and b are BM25's standard tuning knobs — 1.5 and 0.75 are the
    conventional defaults used by, e.g., Elasticsearch and rank_bm25;
    fine to leave alone unless you want to tune them deliberately.
    """

    def __init__(self, documents: list[str], k1: float = 1.5, b: float = 0.75):
        self.k1 = k1
        self.b = b
        self.documents = documents
        self.tokenized_docs = [_tokenize(doc) for doc in documents]
        self.doc_lengths = [len(doc) for doc in self.tokenized_docs]
        self.avg_doc_length = (
            sum(self.doc_lengths) / len(self.doc_lengths) if self.doc_lengths else 0
        )
        self.doc_term_counts = [Counter(doc) for doc in self.tokenized_docs]

        # Inverse document frequency per term, computed once up front.
        n_docs = len(documents)
        df = Counter()
        for doc in self.tokenized_docs:
            for term in set(doc):
                df[term] += 1
        self.idf = {
            term: math.log((n_docs - freq + 0.5) / (freq + 0.5) + 1)
            for term, freq in df.items()
        }

    def _score(self, query_terms: list[str], doc_index: int) -> float:
        score = 0.0
        term_counts = self.doc_term_counts[doc_index]
        doc_length = self.doc_lengths[doc_index]
        for term in query_terms:
            if term not in term_counts:
                continue
            freq = term_counts[term]
            idf = self.idf.get(term, 0.0)
            numerator = freq * (self.k1 + 1)
            denominator = freq + self.k1 * (
                1 - self.b + self.b * doc_length / (self.avg_doc_length or 1)
            )
            score += idf * numerator / denominator
        return score

    def rank(self, query: str) -> list[int]:
        """Returns document indices into `self.documents`, best match first."""
        query_terms = _tokenize(query)
        scored = [
            (self._score(query_terms, i), i) for i in range(len(self.documents))
        ]
        scored.sort(key=lambda pair: pair[0], reverse=True)
        return [i for score, i in scored if score > 0]


def reciprocal_rank_fusion(
    *rankings: list[int], k: int = 60, weights: list[float] | None = None
) -> list[tuple[int, float]]:
    """
    Combine any number of rankings (each a list of doc indices, best-first)
    into one fused ranking. k=60 is the constant used in the original RRF
    paper and is not sensitive to small changes — no need to tune it.

    `weights`, if given, must have one entry per ranking (same order) and
    scales that ranking's contribution — e.g. weights=[1.0, 0.5] trusts the
    first ranking twice as much as the second. Defaults to equal weight
    (1.0 each) for every ranking, matching the original unweighted RRF.
    This is the lever for cases like BM25 confidently but wrongly matching
    on generic vocabulary shared across many documents: rather than letting
    it override a semantic ranking that already got it right, give it less
    say in the fused outcome.

    Returns (doc_index, fused_score) pairs sorted best-first. A doc that
    appears near the top of EITHER ranking gets a boost; a doc that appears
    near the top of BOTH gets boosted twice.
    """
    if weights is None:
        weights = [1.0] * len(rankings)
    if len(weights) != len(rankings):
        raise ValueError("weights must have exactly one entry per ranking")

    scores: dict[int, float] = {}
    for ranking, weight in zip(rankings, weights):
        for rank, doc_index in enumerate(ranking):
            scores[doc_index] = scores.get(doc_index, 0.0) + weight / (k + rank + 1)
    return sorted(scores.items(), key=lambda pair: pair[1], reverse=True)
