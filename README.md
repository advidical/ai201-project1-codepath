# The Unofficial Guide

<!-- Alex D. Lopez - campus_life -->

> **This file is your submission.** Fill it in as you go — most sections get
> written during the milestone that produces them, not at the end.
>
> How the starter works, and every command you'll need, is in `RUNNING.md`.
> Leave that file alone.
>
> **Paste everything as text.** No screenshots, no video. A typed table gets
> full credit; a picture of the same table gets none.
>
> Delete these instruction blocks as you replace them. The `<!-- -->` comments
> are notes to you and don't show up when the page renders — you can leave them
> or remove them.

---

# Unit 1

## What This Does

<!-- Three or four sentences. Which corpus you picked, and the kinds of
     questions your system answers. Write it for someone who has never seen
     this repo.

     I chose the campus corpus for the relatively small chunking size I could use
     to curate my chunks.

     Milestone 5. -->

## Chunking Strategy

**Chunk size:**
**Overlap:**

<!--
     I chose to modify my chunking params to reflect the campus corpus small
     document size, so I chose chunk_size = 350 & chunk_overlap = 50
     These were initially chosen arbitrarily based on intuition and checking the
     initial chunking function, but I verified through claude that these work for
     two reasons:
     1. since the docs average around 320 chars (longest around 550 chars), this
     gurantees the majority of corpus docs fit in a single chunk (header + full body, no splitting at all) — only the longest ~1/3 need to split into two. That's good: over-chunking short documents just multiplies near-duplicate embeddings for no retrieval benefit.

     2. overlap of 50 is 14% of 350 — right in the commonly-cited 10–20% band in the industry.

     In terms of the actual strategy, I wanted to use a sentence based chunker, one that first
     splits the documents into lines, then adds sentences at a time until chunk size reached,
     with a guranteed one sentence (even if it goes over). I used claude to help finish the function, and provide much needed utility functions.

     Milestone 3. -->

## Sample Chunks

<!-- Five chunks, pasted as text. Label each one and name the file it came from
     AND the function that produced it — the grader checks your code against
     what you claim here.

     `python app.py chunks -n 5` prints all three for you. Copy them straight
     across.

     Milestone 3. -->

**Chunk 1** — source: admin_add_drop_deadline.txt#0 ` — produced by: chunker.py::split_documents`
On the add/drop deadline
You can add a course through the end of the second week. Dropping is a longer window — through the end of week six — but a drop after week two shows as a W on your transcript. Nothing anywhere on the registrar's site says this plainly, and students find out from each other.

**Chunk 2** - source: course_cs_210.txt#1 ` — produced by: chunker.py::split_documents`
CS 210 Data Structures
Midterms are curved, the final is not. Expect 8 to 10 hours a week outside class. The one piece of advice: do the labs even though they're only 10% — the exams reuse the lab problems.

**Chunk 3** - source: course_phys_130.txt#0 ` — produced by: chunker.py::split_documents`
PHYS 130 Mechanics
Just finished a year in this building. Format is lecture with a compulsory lab that meets fortnightly. Assessment: three midterms, no final, plus a lab practical. Not curved, but the lowest midterm is dropped. Expect 7 hours a week, plus 3 on lab weeks.

**Chunk 4** - source: dining_the_ridgeway_cafe_followup.txt#0 ` — produced by: chunker.py::split_documents`
Re: The Ridgeway Café
Adding to what people have said about The Ridgeway Café. The wait figure of 10 to 15 minutes at 12:30 matches what I've seen. If you're trying to eat between classes, go before 11:45 and it's a different building entirely. Also worth saying: seating is tight; about 40 seats for a building of 900.

**Chunk 5** - source: housing_innisfree_hall_noise.txt#0 ` — produced by: chunker.py::split_documents`
Noise levels in Innisfree Hall
Asked about this a lot so writing it down. Moderate; the building is l-shaped and the short wing is much quieter. If you're someone who needs quiet to work, the library is open until 2am during term and that's what most people in this building end up doing.

## Sample Answer

<!-- One complete question and answer, pasted as text, with the source line
     visible. Milestone 4. -->

**Question: What do students say about the quality & selection of food at \
 the Kestral Commons during lunch?**

\*\*Answer:

(best distance 0.467, cutoff 0.6)

Based on the documents, students recommend the made-to-order stir-fry station as the thing worth going for, but note that the salad bar wilts after 1:30.

Source: `dining_kestrel_commons.txt`

Sources retrieved: dining_kestrel_commons.txt, dining_kestrel_commons_followup.txt, dining_north_kitchen_followup.txt, dining_the_atrium_followup.txt

1 model calls this session, 692 tokens (639 in, 53 out)\*\*

```

```

**My relevance cutoff:**

<!-- The number you set in config.py, and how you got there.

     You ran five questions your corpus covers and the five in OUT_OF_SCOPE
     that it clearly doesn't, and wrote down the best distance for each. What
     did those two groups look like? Where was the gap? Put the actual numbers
     here — the table below wants all ten rows.

     Milestone 4. -->

     So I decided to keep my relevance cutoff around 0.6 since it seems that
     it's well within my gap between my questions and the out of scope questions
     I will note that I did change one of my questions halfway through, but I kept one
     that is above the relevance cutoff and decided to keep it since it's an example of a
     question that the corpus could've answered but didn't have enough relevant information
     to reach that consensus, which I thought was very interesting but ultimately made sense
     given the context and the fact the docs don't talk much about the advisors.

| Question                                                                                                                                                              | In corpus?   | Best distance |
| --------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------ | ------------- |
| What do students say about the quality & selection of food at the Kestral Commons during lunch?                                                                       | Yes          | 0.4666        |
| What do students say about the amount of study time needed outside of class each week for computer science courses?                                                   | Yes          | 0.4036        |
| What do students say about the overall dining experience at campus, when it comes to dining halls on campus, cost of meal plans, and accessibility of dining dollars? | Yes          | 0.4404        |
| What do students say about the accessibility & operating hours of the transit shuttle on campus?                                                                      | Yes          | 0.3710        |
| What do students recommend to do to have access to advisers with better tailored guidance for their major?                                                            | No (refused) | 0.7252        |
| What is the capital of Mongolia?                                                                                                                                      | No (refused) | 0.8246        |
| Who won the 1994 World Cup?                                                                                                                                           | No (refused) | 0.8859        |
| How do I change the oil in a diesel engine?                                                                                                                           | No (refused) | 0.9323        |
| What is the recommended dosage of ibuprofen for a headache?                                                                                                           | No (refused) | 0.8477        |
| How do I write a for loop in Rust?                                                                                                                                    | No (refused) | 0.8907        |
|                                                                                                                                                                       |              |               |

## How I Used AI

<!-- Two specific moments. For each: what you asked for, what came back, and
     what you changed about it.

     "I asked Claude to write the chunking function from my notes. It ignored
     the overlap, so I added that myself" is the level of detail we're after.
     "I used AI to help me code" is not.

     Milestone 5. -->

**1. I asked claude to help me make the chunking function based on what I was after:
Creating a chunking strategy that seperated the docs by lines, then chunked by sentences.
It gave me that and information regarding how my chunking params that I chose arbitrarily
based on reading the campus corpus fit to industry standards and practices. Only thing I changed
were the comments so that they had more brevity and didn't clog space.**

**2. I asked claude to help quickly format my relevance cutoff table so that I could quickly copy
and paste since I was running low on time & I had already pasted my results from testing
my questions into a document. It did save me time. I didn't really change anything from the results since I just needed a quick formatting to save time.**

<!-- ── Stretch features ─────────────────────────────────────────────────────
     Doing one? Say so here BEFORE you start. A feature this README never
     claims earns nothing.
     ───────────────────────────────────────────────────────────────────────── -->

---

# Unit 2

<!-- These sections get ADDED to what's already above. Don't delete or rewrite
     unit 1 — the point is that someone can see what you said before you knew
     how it went. -->

## Run Log — Before

<!-- Your five criteria, three runs each. `python run_eval.py --label before`
     runs the questions, puts the OUT_OF_SCOPE ones through the gate, and
     writes it all into results/ for you. Targets come from criteria.md; the
     verdict column is your call.

     Criterion 3 is measured in one deterministic pass rather than three, so
     the same number goes in all three run columns. That's correct, not lazy.

     Milestone 1. -->

| Criterion                              | Target | Run 1 | Run 2 | Run 3 | Verdict |
| -------------------------------------- | ------ | ----- | ----- | ----- | ------- |
| 1. Retrieved chunk contains the answer | 4 of 5 |       |       |       |         |
| 2. Every answer names a source         | 5 of 5 |       |       |       |         |
| 3. Gate stops out-of-corpus questions  | 4 of 5 |       |       |       |         |
| 4.                                     |        |       |       |       |         |
| 5.                                     |        |       |       |       |         |

<!-- Underneath, paste the REAL output for each criterion from one of your
     runs — the actual text your system produced, not a description of it.
     Name the file and function that produced it. -->

## Verdicts

<!-- MET or MISSED for each of the five, against the target you wrote last
     unit — not a new one. Plus a sentence on how you decided. That sentence
     matters most where it was close.

     If your target said 4 of 5 and your runs came out 4, 3, 4, that's a MISS.
     The target has to hold, not show up occasionally.

     Milestone 2. -->

| #   | Criterion | Verdict | How I decided |
| --- | --------- | ------- | ------------- |
| 1   |           |         |               |
| 2   |           |         |               |
| 3   |           |         |               |
| 4   |           |         |               |
| 5   |           |         |               |

## Diagnoses

<!-- For each miss: which stage caused it, and how. The stage alone isn't
     enough — you need the mechanism.

     Not a diagnosis: "Question 3 didn't work."
     A diagnosis:     "Question 3 asks about laundry costs. The answer is in
                       one sentence that got split across two chunks, so
                       neither chunk on its own contains it."

     The five stages: loading → chunking → embedding → retrieval → generation.

     Look for a pattern. If three misses all ask about numbers, that's one
     problem, not three.

     Missed nothing? Say so, then say honestly whether your targets were set
     low, and which one you'd tighten and to what.

     Milestone 3. -->

## The Improvement

**What I changed:**

**Why I picked it:**

<!-- Connect it to a specific diagnosis above in one sentence. If you can't,
     you picked a fix because it sounded impressive. -->

### Run Log — After

<!-- Same format, same five criteria, three runs each.
     `python run_eval.py --label after` -->

| Criterion                              | Target | Run 1 | Run 2 | Run 3 | Verdict |
| -------------------------------------- | ------ | ----- | ----- | ----- | ------- |
| 1. Retrieved chunk contains the answer | 4 of 5 |       |       |       |         |
| 2. Every answer names a source         | 5 of 5 |       |       |       |         |
| 3. Gate stops out-of-corpus questions  | 4 of 5 |       |       |       |         |
| 4.                                     |        |       |       |       |         |
| 5.                                     |        |       |       |       |         |

**Did it help?**

<!-- Say plainly whether it did, and how you know. If it made things worse,
     say that — a change that backfired, honestly reported, earns full credit
     and is more interesting than one that worked. What matters is that you can
     tell.

     Milestone 4. -->

## What's Still Broken

<!-- For each criterion still missed after your fix: what you'd do about it,
     and why you stopped where you did.

     "I ran out of time" is fine if it's true. Pretending nothing is left is
     not.

     Milestone 5. -->

## What I'd Do Differently

<!-- Knowing what you know now — which of your five criteria would you write
     differently, and why?

     Milestone 5. -->
