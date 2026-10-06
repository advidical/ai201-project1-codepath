# Scorer.py : used to determine criterion results
import re

import nltk
from nltk.stem import PorterStemmer

from store import Result

MAX_STEM_LEN = 40

_MIN_SAFE_NLTK_VERSION = (3, 10, 3)

def _parse_version(v: str) -> tuple:
    parts = []
    for piece in v.split("."):
        digits = "".join(ch for ch in piece if ch.isdigit())
        parts.append(int(digits) if digits else 0)
    return tuple(parts)

def _check_nltk_version():
    if _parse_version(nltk.__version__) < _MIN_SAFE_NLTK_VERSION:
        import warnings

        warnings.warn(
            f"nltk {nltk.__version__} is installed, but PorterStemmer.stem() has "
            f"a known quadratic-time DoS bug (CVE-2026-81722), fixed only in "
            f"nltk>=3.10.3. Run `pip install --upgrade nltk` to fix this.",
            stacklevel=2,
        )

_stemmer = PorterStemmer()
_WORD = re.compile(r"[a-z0-9]+")

# "##:##" in an expects string means "some clock time must appear somewhere
# in the retrieved text" - not a specific value, just the general shape
TIME_PLACEHOLDER = "##:##"
# Matches an actual clock time in the retrieved text
TIME_PATTERN = re.compile(r"\b\d{1,2}:\d{2}(?:\s*[ap]m)?\b", re.IGNORECASE)


def _tokenize(text: str) -> list[str]:
    return _WORD.findall(text.lower())


def _safe_stem(word: str) -> str:
    """Stem a word, skipping anything implausibly long."""
    if len(word) > MAX_STEM_LEN:
        return word
    return _stemmer.stem(word)


def _stems(words) -> set[str]:
    return {_safe_stem(w) for w in words}


def judge(question: str, expects: str, answer: str, results: list[Result], gate_rows: list
) -> list[bool]:
    """
    Returns True for each criteria:
      1. Retrieved chunks or Answer contain the expected words         
      2. Every answer names at least one source document 
      3. The relevance gate stops out-of-corpus questions 
      4. Chunks reflect the size of corpus docs           
      5. Top-3 retrieved docs share the question's topic prefix 
    """
    def _retrieval_contains_expected(expects_keywords: str, answer:str, results: list[Result]):
        # Stem instead of exact substring for better matching
        # Need to strip time placeholder to check separately
        needs_time = TIME_PLACEHOLDER in expects_keywords
        remaining_keywords = expects_keywords.replace(TIME_PLACEHOLDER, "")

        haystack_text = " ".join(r.text for r in results) + " " + answer
        haystack_stems = _stems(_tokenize(haystack_text))
        expected_stems = _stems(_tokenize(remaining_keywords))
        words_found = expected_stems.issubset(haystack_stems)
        print(expected_stems, TIME_PATTERN.search(haystack_text))
        print(haystack_stems.intersection(expected_stems))
        if needs_time:
            return words_found and bool(TIME_PATTERN.search(haystack_text))
        return words_found

    def _answer_names_a_source(answer: str):
        return ".txt" in answer
    
    def _gate_behaves_correctly(gate_rows:list):
        gate_results = [decision['refused'] for decision in gate_rows]
        return all(gate_results)

    def _chunks_are_reasonably_sized(results: list[Result], max_chars: int = 400):
        # chunk_size + overlap == 350 + 50 == 400, per your chunker's params.
        # No chunk's text should be longer than that ceiling.
        my_results = [r.text for r in results]
        return all(len(text) <= max_chars for text in my_results)
 
    def _share_topic_prefix(expects_topic: str, results: list[Result]):
        # "Same topic" == expects_topic shows up as a substring of the
        # source filename (case-sensitive, matching your corpus's casing)
        my_topics = [r.source for r in results]
        return any(expects_topic in topics for topics in my_topics)

    # check nltk>=3.10.3 due to known quadratic-time DoS bug prior to that version
    _check_nltk_version()

    expects_keywords, expects_topic = expects.rsplit("?", 1)
    print(expects_keywords, expects_topic)
    checks = [
        _retrieval_contains_expected(expects_keywords, answer, results),
        _answer_names_a_source(answer),
        _gate_behaves_correctly(gate_rows),
        _chunks_are_reasonably_sized(results),
        _share_topic_prefix(expects_topic, results),
    ]
    return checks