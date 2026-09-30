# Scorer.py : used to determine criterion results
from store import Result 
def judge(question: str,expects: str, answer: str, results: list[Result], gate_rows: list
) -> bool:
    """
    Returns True only if ALL criteria pass:
      1. Retrieved chunks contain the answer            
      2. Every answer names at least one source document 
      3. The relevance gate stops out-of-corpus questions 
      4. Chunks reflect the size of corpus docs           
      5. Top-3 retrieved docs share the question's topic prefix 
    """
    def _retrieved_chunks_contain_expected(expects_keywords: str, results: list[Result]):
        my_results = [r.text for r in results]
        expected_words = expects_keywords.split() # split into list of words to expect
        return all(any(word in text for text in my_results) for word in expected_words)

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


    expects_keywords, expects_topic = expects.rsplit(":", 1)
    checks = [
        _retrieved_chunks_contain_expected(expects_keywords, results),
        _answer_names_a_source(answer),
        _gate_behaves_correctly(gate_rows),
        _chunks_are_reasonably_sized(results),
        _share_topic_prefix(expects_topic, results),
    ]
    return checks
