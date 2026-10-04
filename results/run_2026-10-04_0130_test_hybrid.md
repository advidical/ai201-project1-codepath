# Run log — test_hybrid

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `campus_life` (index variant `default`)
- top-k: 5 · relevance cutoff: 0.75
- Runs per question: 3, caching off
- When: 2026-10-04 01:30

This table is one row per QUESTION. The run log your README asks for is
one row per CRITERION, so aggregate these into it — criterion 1 is how many
of your questions had the answer in the retrieved chunks, and so on.

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| What do students say about the quality & selection of food at      the Kestrel Commons during lunch? | pass | pass | pass |
| What do students say about the amount of study time needed outside of class     each week for computer science courses? | pass | pass | pass |
| What do students say about the accessibility & operating hours of the      transit shuttle on campus? | pass | pass | pass |
| What advice do students most commonly leave when it comes to registering for      your courses & picking your adviser? | pass | pass | pass |
| What do students say about the overall dining experience at campus, when     it comes to dining halls on campus, cost of meals plans, and accessibility of dining dollars? | pass | pass | pass |

---

## The relevance gate on out-of-corpus questions

Produced by `run_eval.py::check_out_of_scope`, cutoff 0.75. Refused 5 of 5.

Retrieval is deterministic and the gate is a comparison against a
fixed number, so these do not vary between runs — one pass over the
list is the whole measurement.

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.861 | refused |
| How do I change the oil in a diesel engine? | 0.902 | refused |
| Who won the 1994 World Cup? | 0.880 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.866 | refused |
| How do I write a for loop in Rust? | 0.878 | refused |

---

## Real output

This is what the system actually produced. Paste the relevant parts
into your README underneath the table — the rubric asks for real
output as text, not a description of it.

### What do students say about the quality & selection of food at      the Kestrel Commons during lunch? — run 1

- Best distance: 0.6459 (passed the gate)
- Sources retrieved: admin_housing_lottery.txt, dining_kestrel_commons.txt, dining_kestrel_commons_followup.txt, dining_verrill_street_grill.txt

```
Students state that the stir-fry station (which is made to order) is worth going for, but they also note that the salad bar wilts after 1:30. 

This information comes from the document `dining_kestrel_commons.txt`.
```

### What do students say about the quality & selection of food at      the Kestrel Commons during lunch? — run 2

- Best distance: 0.6459 (passed the gate)
- Sources retrieved: admin_housing_lottery.txt, dining_kestrel_commons.txt, dining_kestrel_commons_followup.txt, dining_verrill_street_grill.txt

```
Students mention that the stir-fry station (which is made to order) is worth going for, but the salad bar wilts after 1:30 (dining_kestrel_commons.txt and dining_kestrel_commons_followup.txt).
```

### What do students say about the quality & selection of food at      the Kestrel Commons during lunch? — run 3

- Best distance: 0.6459 (passed the gate)
- Sources retrieved: admin_housing_lottery.txt, dining_kestrel_commons.txt, dining_kestrel_commons_followup.txt, dining_verrill_street_grill.txt

```
Based on the documents, students state that the stir-fry station (which is made to order) is worth going for, but the salad bar wilts after 1:30. 

This comes from `dining_kestrel_commons.txt` and `dining_kestrel_commons_followup.txt`.
```

### What do students say about the amount of study time needed outside of class     each week for computer science courses? — run 1

- Best distance: 0.5968 (passed the gate)
- Sources retrieved: course_cs_210.txt, course_cs_210_workload.txt, course_econ_101_workload.txt, course_stat_150_workload.txt

```
For the CS 210 Data Structures course, students can expect 8 to 10 hours a week outside of class, and this workload is front-loaded with the first month being heavier (course_cs_210_workload.txt and course_cs_210.txt).
```

### What do students say about the amount of study time needed outside of class     each week for computer science courses? — run 2

- Best distance: 0.5968 (passed the gate)
- Sources retrieved: course_cs_210.txt, course_cs_210_workload.txt, course_econ_101_workload.txt, course_stat_150_workload.txt

```
For CS 210 Data Structures, students should expect 8 to 10 hours a week outside of class (source: `course_cs_210_workload.txt` and `course_cs_210.txt`).
```

### What do students say about the amount of study time needed outside of class     each week for computer science courses? — run 3

- Best distance: 0.5968 (passed the gate)
- Sources retrieved: course_cs_210.txt, course_cs_210_workload.txt, course_econ_101_workload.txt, course_stat_150_workload.txt

```
For CS 210 Data Structures, students should expect 8 to 10 hours a week outside of class (source: `course_cs_210_workload.txt` and `course_cs_210.txt`).
```

### What do students say about the accessibility & operating hours of the      transit shuttle on campus? — run 1

- Best distance: 0.6389 (passed the gate)
- Sources retrieved: admin_study_abroad.txt, dining_the_ridgeway_cafe.txt, transit_shuttle.txt, transit_walking.txt

```
Based on the documents, the campus shuttle runs a loop every 20 minutes from 7:00 am to 11:00 pm on weekdays and every 40 minutes on weekends. Its published timetable is optimistic by about five minutes in the morning and accurate the rest of the day, and it is free with a student ID. 

Source: `transit_shuttle.txt`
```

### What do students say about the accessibility & operating hours of the      transit shuttle on campus? — run 2

- Best distance: 0.6389 (passed the gate)
- Sources retrieved: admin_study_abroad.txt, dining_the_ridgeway_cafe.txt, transit_shuttle.txt, transit_walking.txt

```
Students say the campus shuttle runs a loop every 20 minutes from 7:00 am to 11:00 pm on weekdays and every 40 minutes on weekends. It is free with a student ID, and the published timetable is optimistic by about five minutes in the morning and accurate the rest of the day. 

Source: `transit_shuttle.txt`
```

### What do students say about the accessibility & operating hours of the      transit shuttle on campus? — run 3

- Best distance: 0.6389 (passed the gate)
- Sources retrieved: admin_study_abroad.txt, dining_the_ridgeway_cafe.txt, transit_shuttle.txt, transit_walking.txt

```
According to transit_shuttle.txt, the campus shuttle runs a loop every 20 minutes from 7am to 11pm on weekdays and every 40 minutes on weekends. Regarding accessibility, it is free with a student ID, its published timetable is optimistic by about five minutes in the morning and accurate for the rest of the day, and the stop outside Fenwick Court is skipped if the driver is behind.
```

### What advice do students most commonly leave when it comes to registering for      your courses & picking your adviser? — run 1

- Best distance: 0.7334 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_study_abroad.txt, admin_withdrawal_deadline.txt, advising_registration.txt, orientation_what_matters.txt

```
Based on the provided documents, students are advised to book their adviser two weeks out, because advisers get busy in the week before registration opens, and you need your adviser hold lifted before you can register. 

Source: `advising_registration.txt`
```

### What advice do students most commonly leave when it comes to registering for      your courses & picking your adviser? — run 2

- Best distance: 0.7334 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_study_abroad.txt, admin_withdrawal_deadline.txt, advising_registration.txt, orientation_what_matters.txt

```
Based on the documents, you need your adviser hold lifted before you can register, and since advisers get very busy in the week before registration opens, you should book two weeks out (*advising_registration.txt*). Additionally, registration times are staggered by credit hours, and popular courses tend to fill up in the first two days (*advising_registration.txt*).
```

### What advice do students most commonly leave when it comes to registering for      your courses & picking your adviser? — run 3

- Best distance: 0.7334 (passed the gate)
- Sources retrieved: admin_add_drop_deadline.txt, admin_study_abroad.txt, admin_withdrawal_deadline.txt, advising_registration.txt, orientation_what_matters.txt

```
According to *advising_registration.txt*, students are advised to book their adviser two weeks out because advisers get busy the week before registration opens, and an adviser hold must be lifted before you can register.
```

### What do students say about the overall dining experience at campus, when     it comes to dining halls on campus, cost of meals plans, and accessibility of dining dollars? — run 1

- Best distance: 0.7064 (passed the gate)
- Sources retrieved: admin_dining_dollars.txt, dining_pellew_dining_hall.txt, dining_pellew_dining_hall_followup.txt, housing_tamsin_court.txt, money_jobs.txt

```
Based on the provided documents:

* **Dining halls:** Pellew Dining Hall is the furthest hall from anywhere and is located next to the athletics centre. It has peak wait times of 12 to 18 minutes, though going before 11:45 avoids this rush. It costs one meal swipe or $11.75 cash. (*dining_pellew_dining_hall.txt*, *dining_pellew_dining_hall_followup.txt*)
* **Cost of meal plans / Dining dollars:** Dining dollars roll over from the autumn semester to the spring semester, but whatever is left in May disappears and does not roll over to the following autumn. (*admin_dining_dollars.txt*)
```

### What do students say about the overall dining experience at campus, when     it comes to dining halls on campus, cost of meals plans, and accessibility of dining dollars? — run 2

- Best distance: 0.7064 (passed the gate)
- Sources retrieved: admin_dining_dollars.txt, dining_pellew_dining_hall.txt, dining_pellew_dining_hall_followup.txt, housing_tamsin_court.txt, money_jobs.txt

```
Based on the provided documents:

* **Dining halls:** Pellew Dining Hall is the furthest hall from anywhere and is located next to the athletics centre. During peak times, wait times are 12 to 18 minutes, but going before 11:45 avoids this (dining_pellew_dining_hall_followup.txt and dining_pellew_dining_hall.txt). It costs one meal swipe or $11.75 cash (dining_pellew_dining_hall.txt). 
* **Cost of meals and dining dollars:** Dining dollars (declining balance) roll over from the autumn semester to the spring, but any remaining balance in May disappears and does not roll over to the following autumn (admin_dining_dollars.txt).
```

### What do students say about the overall dining experience at campus, when     it comes to dining halls on campus, cost of meals plans, and accessibility of dining dollars? — run 3

- Best distance: 0.7064 (passed the gate)
- Sources retrieved: admin_dining_dollars.txt, dining_pellew_dining_hall.txt, dining_pellew_dining_hall_followup.txt, housing_tamsin_court.txt, money_jobs.txt

```
Based on the provided documents, students note that Pellew Dining Hall has peak wait times of 12 to 18 minutes, is the furthest dining hall from everything (located next to the athletics centre), and costs one meal swipe or $11.75 in cash per meal (*dining_pellew_dining_hall.txt* and *dining_pellew_dining_hall_followup.txt*). Regarding dining dollars, declining balances roll over from the autumn semester to the spring semester, but any remaining amount in May disappears and does not roll over to the following autumn (*admin_dining_dollars.txt*).
```
