"""
Stage 2 of the pipeline: splitting documents into chunks.

⚠️ THIS IS THE FILE YOU CHANGE IN MILESTONE 3.

`split_documents` below is deliberately plain. It cuts every document into
fixed-size pieces with a fixed overlap and pays no attention to where sentences
or paragraphs end. It works, and it is not good.

On a corpus of short posts it may not cut anything at all: `campus_life` comes
out as 88 documents and 88 chunks, because almost nothing in it reaches 800
characters. That is the baseline, not a bug — Milestone 3 is where you decide
whether one post should stay one chunk.

Your job in Milestone 3 is to replace the *body* of `split_documents` with a
strategy that fits the documents you actually read in Milestone 1. Keep the
name and the shape of what it returns — the rest of the pipeline calls it, and
your README has to name the function that produced your chunks.

If you get stuck for 30 minutes, `fallback_split` is the original. Switch back
to it, write down what you saw, and move on. That's a real observation about
your pipeline, not giving up.
"""

from dataclasses import dataclass

import config
from ingest import Document
import nltk
from functools import lru_cache

@dataclass
class Chunk:
    """One piece of one document."""

    text: str
    source: str        # which file it came from
    index: int         # which chunk within that file, starting at 0
    produced_by: str   # the function that made it — cite this in your README

    @property
    def label(self) -> str:
        return f"{self.source}#{self.index}"


def fallback_split(
    documents: list[Document],
    chunk_size: int | None = None,
    overlap: int | None = None,
) -> list[Chunk]:
    """
    The starter's original chunker. Fixed-size character windows with overlap.

    Keep this function. Milestone 3's stop rule points back at it, and having
    something to compare your own strategy against is useful in unit 2.
    """
    chunk_size = chunk_size or config.CHUNK_SIZE
    overlap = overlap or config.CHUNK_OVERLAP

    if overlap >= chunk_size:
        raise ValueError("overlap has to be smaller than chunk_size")

    chunks: list[Chunk] = []
    for doc in documents:
        start = 0
        index = 0
        while start < len(doc.text):
            piece = doc.text[start : start + chunk_size].strip()
            if piece:
                chunks.append(
                    Chunk(
                        text=piece,
                        source=doc.source,
                        index=index,
                        produced_by="chunker.py::fallback_split",
                    )
                )
                index += 1
            start += chunk_size - overlap

    return chunks


"""
split_documents — a header-anchored, sentence-aware chunking strategy.
"""

from functools import lru_cache

@lru_cache(maxsize=1)
def _ensure_nltk_ready() -> None:
    # nltk's sentence tokenizer needs a one-time data download ("punkt_tab" as of
    # nltk >= 3.9; older nltk versions use "punkt")
    # Download only happens once per machine, not once per call
    try:
        nltk.data.find("tokenizers/punkt_tab")
    except LookupError:
        nltk.download("punkt_tab", quiet=True)


def _split_into_sentences(line: str) -> list[str]:
    """Split a single line into sentence-sized pieces, dropping empties."""
    _ensure_nltk_ready()
    pieces = nltk.sent_tokenize(line.strip())
    return [p.strip() for p in pieces if p.strip()]


def split_documents(
    documents: list[Document],
    chunk_size: int | None = None,
    overlap: int | None = None,
) -> list[Chunk]:
    """
    Header-anchored, sentence-aware chunker for short, line-delimited docs
    (e.g. one student review per file, first line = header).

    Strategy:
      1. Treat each file's first non-empty line as its header. Every chunk
         emitted for this doc gets that header prepended, so a chunk can
         always be traced back to its source topic even out of context.
      2. Treat the remaining lines as the "pre-chunked" units the corpus is
         already naturally divided into. (assumes newline delimited corpus)
      3. Within those lines, split down to sentences — the smallest unit we
         are willing to hand back to the retriever — and greedily pack
         sentences into a chunk until adding one more would blow the
         chunk_size budget (header included in that budget).
      4. Every chunk is guaranteed at least one full sentence, even if that
         single sentence alone (plus header) exceeds chunk_size — we never
         cut a sentence in half.
      5. Consecutive chunks share a sentence-aligned overlap of up to
         `overlap` characters, so an idea that lands right at a chunk
         boundary still appears whole in at least one chunk.

    Defaults (350 / 50) are tuned for this corpus: short reviews averaging
    ~320 chars, longest ~550 chars for default chunking strat in fallback_split
    """
    chunk_size = chunk_size or config.CHUNK_SIZE
    overlap = overlap or config.CHUNK_OVERLAP

    if overlap >= chunk_size:
        raise ValueError("overlap has to be smaller than chunk_size")

    chunks: list[Chunk] = []

    for doc in documents:
        # --- Step 1: pull out header vs. body ---
        lines = [ln.strip() for ln in doc.text.split("\n") if ln.strip()]
        if not lines:
            continue  # empty doc, nothing to chunk

        header = lines[0]
        body_lines = lines[1:] if len(lines) > 1 else []

        # --- Step 2: flatten body lines into a flat list of sentences ---
        sentences: list[str] = []
        for line in body_lines:
            sentences.extend(_split_into_sentences(line))

        if not sentences:
            # Doc was just a header with no body content
            sentences = [header]

        # --- Steps 3/4: greedily pack sentences into size-bounded chunks ---
        index = 0
        i = 0
        n = len(sentences)

        while i < n:
            current: list[str] = []
            body_len = 0
            j = i

            while j < n:
                candidate = sentences[j]
                sep_len = 1 if current else 0  # space joining sentences
                new_body_len = body_len + sep_len + len(candidate)
                # header + "\n" + body, measured against chunk_size
                prospective_total = len(header) + 1 + new_body_len

                if current and prospective_total > chunk_size:
                    # Adding this sentence would overflow the budget, and we
                    # already have >=1 sentence in this chunk — stop here.
                    break

                # Either we're under budget, or this is the first sentence
                # in the chunk ("min one sentence" guarantee, regardless of overflow)
                current.append(candidate)
                body_len = new_body_len
                j += 1

            body_text = " ".join(current)
            chunks.append(
                Chunk(
                    text=f"{header}\n{body_text}",
                    source=doc.source,
                    index=index,
                    produced_by="chunker.py::split_documents",
                )
            )
            index += 1

            if j >= n:
                break  # consumed the whole doc

            # --- Step 5: compute sentence-aligned overlap for next window ---
            # Create sliding window going from (j-1) towards start(i)
            # Creating windows of overlap chars, adding 1 sentence at a time
            overlap_chars = 0
            k = j - 1
            while k > i and overlap_chars < overlap:
                overlap_chars += len(sentences[k]) + 1
                k -= 1

            # Next window starts at k+1 (the first sentence to re-include), 
            # but must move forward by at least one sentence, or
            # risk infinite loop on one over-sized sentence
            i = max(k + 1, i + 1)

    return chunks


def describe(chunks: list[Chunk]) -> str:
    """A one-line summary, printed after indexing."""
    if not chunks:
        return "0 chunks"
    lengths = [len(c.text) for c in chunks]
    return (
        f"{len(chunks)} chunks, "
        f"{sum(lengths) // len(lengths)} characters on average "
        f"(shortest {min(lengths)}, longest {max(lengths)}), "
        f"produced by {chunks[0].produced_by}"
    )


if __name__ == "__main__":
    from ingest import load_documents

    chunks = split_documents(load_documents())
    print(describe(chunks))
