# Acceptance criteria — The Unofficial Guide

Five criteria that say what "working" means for this system, written in unit 1
**before** any results existed.

An acceptance criterion names a target: a number, a count, a rate, or something
a person could plainly observe. _"Retrieval works"_ is an opinion. _"For at
least 4 of my 5 test questions, the top results include a chunk containing the
answer"_ is a criterion.

Under each one, write a sentence or two on **why that target** and not a
stricter or looser one. A reason that says something about your corpus or your
pipeline earns credit; _"80% seemed reasonable"_ does not.

> Missing your own targets next unit costs you nothing. Setting a target so
> easy you can't miss it does.

---

## 1. Retrieved chunks contain the answer

For at least 4 of my 5 test questions, the retrieved chunks include one that
contains the answer.

**Why this target:**

<!-- I picked 4 of 5 because one of my questions is about a
     topic that includes two different prefix documents, admin & dining.
     I want to see if the model can understand the relationship between
     dining prefix documents and admin_dining documents and provide at least
     specific points of the campus dining experience. -->

---

## 2. Every answer names a source

Every answer the system produces names at least one source document.

**Why this target:**

<!-- I want to understand the model and what it gets right and wrong,
     as in understanding how it adapts to scope. -->

---

## 3. The relevance gate stops out-of-corpus questions

When I ask a question my documents clearly don't cover, the relevance gate
stops it and the system returns "I don't have enough information about that" —
in at least 4 of 5 tries.

<!-- The five questions are the ones in `OUT_OF_SCOPE` at the bottom of
     `questions.py`, and `run_eval.py` puts them through the gate and writes
     what happened into your run log. Swap them for your own if you'd rather —
     just keep five of them, or the "4 of 5" above has nothing to be 4 of. -->

**Why this target:**

<!-- My question regarding dining experience at campus is very general and does ask
for an overall view, so I want to see if it will simply say it cannot make that assessment,
or will say that plus some specific info from the documents to at least provide relevant info
-->

---

## 4. Chunks reflect the size of corpus docs

Every chunk should be between 250 & 500 chars inclusive, to reflect
the short form responses of the corpus documents.

**Why this target:**

<!-- I wanted the chunks to reflect the average char count of the
     campus corpus since it's very short blurbs of info from students, but
     be able to account for questions requiring multiple sources.
-->

---

## 5. Understand topic relevance question fits under

For at least 4 of 5 test questions, all 3 top-ranked retrieved documents have the same predefined topic prefix as the test question (e.g., an admin question retrieves only admin documents).

**Why this target:**

<!--I want my questions to pull the right topic(s) relevant to the question, and see
    how well or badly it does doing so. ->
---

<!-- ─────────────────────────────────────────────────────────────────────────
     UNIT 2 — read this before you change anything above.

     If a criterion turns out to be BROKEN rather than merely unmet, you can
     revise it, and that earns credit. But never delete or edit the original
     line. Add the revision underneath it, like this:

         ## 1. Retrieved chunks contain the answer

         For at least 4 of my 5 test questions, the retrieved chunks include
         one that contains the answer.

         **Why this target:** ...

         > **Revised in unit 2:** For at least 4 of 5 questions, the top three
         > results contain the answer.
         >
         > **Why revised:** I couldn't judge "the chunks include one that
         > contains the answer" the same way twice — I scored two questions
         > differently on Monday than on Wednesday. The new version is
         > something I can actually check.

     That's a revision because the criterion couldn't be MEASURED.

     Lowering a target because you missed it is not a revision, and it costs
     you the point:

         ✗ "I said 4 of 5 but got 2 of 5, so 2 of 5 is more realistic."

     A number you missed stays where it is, gets diagnosed, and gets a fix
     attempted. That's where the points are.

     The whole reason the originals stay visible is so someone can see what you
     said before you knew the answer.
     ───────────────────────────────────────────────────────────────────────── -->
