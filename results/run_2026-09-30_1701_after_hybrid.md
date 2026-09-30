# Run log — after_hybrid

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `campus_life` (index variant `default`)
- top-k: 5 · relevance cutoff: 0.6
- Runs per question: 3, caching off
- When: 2026-09-30 17:01

This table is one row per QUESTION. The run log your README asks for is
one row per CRITERION, so aggregate these into it — criterion 1 is how many
of your questions had the answer in the retrieved chunks, and so on.

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| What do students say about the quality & selection of food at      the Kestral Commons during lunch? | fail | fail | fail |
| What do students say about the amount of study time needed outside of class     each week for computer science courses? | pass | pass | pass |
| What do students say about the accessibility & operating hours of the      transit shuttle on campus? | pass | pass | pass |
| What advice do students most commonly leave when it comes to registering for      your courses & picking your adviser? | pass | pass | pass |
| What do students say about the overall dining experience at campus, when     it comes to dining halls on campus, cost of meals plans, and accessibility of dining dollars? | pass | pass | pass |

---

## The relevance gate on out-of-corpus questions

Produced by `run_eval.py::check_out_of_scope`, cutoff 0.6. Refused 5 of 5.

Retrieval is deterministic and the gate is a comparison against a
fixed number, so these do not vary between runs — one pass over the
list is the whole measurement.

| Out-of-scope question | Best distance | Gate |
|---|---|---|
| What is the capital of Mongolia? | 0.825 | refused |
| How do I change the oil in a diesel engine? | 0.932 | refused |
| Who won the 1994 World Cup? | 0.886 | refused |
| What is the recommended dosage of ibuprofen for a headache? | 0.848 | refused |
| How do I write a for loop in Rust? | 0.891 | refused |

---

## Real output

This is what the system actually produced. Paste the relevant parts
into your README underneath the table — the rubric asks for real
output as text, not a description of it.

### What do students say about the quality & selection of food at      the Kestral Commons during lunch? — run 1

- Best distance: 0.4519 (passed the gate)
- Sources retrieved: dining_halden_hall_followup.txt, dining_kestrel_commons_followup.txt, dining_north_kitchen_followup.txt, dining_the_atrium_followup.txt, dining_the_ridgeway_cafe_followup.txt

```
Based on the provided documents, students note that the salad bar at Kestrel Commons wilts after 1:30 (dining_kestrel_commons_followup.txt).
```

### What do students say about the quality & selection of food at      the Kestral Commons during lunch? — run 2

- Best distance: 0.4519 (passed the gate)
- Sources retrieved: dining_halden_hall_followup.txt, dining_kestrel_commons_followup.txt, dining_north_kitchen_followup.txt, dining_the_atrium_followup.txt, dining_the_ridgeway_cafe_followup.txt

```
Students say that the salad bar at Kestrel Commons wilts after 1:30. 

Source: dining_kestrel_commons_followup.txt
```

### What do students say about the quality & selection of food at      the Kestral Commons during lunch? — run 3

- Best distance: 0.4519 (passed the gate)
- Sources retrieved: dining_halden_hall_followup.txt, dining_kestrel_commons_followup.txt, dining_north_kitchen_followup.txt, dining_the_atrium_followup.txt, dining_the_ridgeway_cafe_followup.txt

```
Based on the documents, students note that the salad bar at Kestrel Commons wilts after 1:30. 

Source: dining_kestrel_commons_followup.txt
```

### What do students say about the amount of study time needed outside of class     each week for computer science courses? — run 1

- Best distance: 0.4077 (passed the gate)
- Sources retrieved: course_cs_210.txt, course_cs_210_workload.txt, course_econ_101_workload.txt, course_stat_150.txt, course_stat_150_workload.txt

```
For CS 210 Data Structures, students should expect 8 to 10 hours a week outside of class (from `course_cs_210.txt` and `course_cs_210_workload.txt`).
```

### What do students say about the amount of study time needed outside of class     each week for computer science courses? — run 2

- Best distance: 0.4077 (passed the gate)
- Sources retrieved: course_cs_210.txt, course_cs_210_workload.txt, course_econ_101_workload.txt, course_stat_150.txt, course_stat_150_workload.txt

```
Based on the documents, students can expect 8 to 10 hours a week outside class for CS 210 Data Structures, which is real time and front-loaded with a heavier first month. 

Sources: `course_cs_210.txt` and `course_cs_210_workload.txt`
```

### What do students say about the amount of study time needed outside of class     each week for computer science courses? — run 3

- Best distance: 0.4077 (passed the gate)
- Sources retrieved: course_cs_210.txt, course_cs_210_workload.txt, course_econ_101_workload.txt, course_stat_150.txt, course_stat_150_workload.txt

```
For CS 210 Data Structures, students should expect to spend 8 to 10 hours a week outside of class. This is real time rather than optimistic time and is front-loaded, meaning the first month is heavier than the rest. 

Sources: `course_cs_210.txt` and `course_cs_210_workload.txt`
```

### What do students say about the accessibility & operating hours of the      transit shuttle on campus? — run 1

- Best distance: 0.3749 (passed the gate)
- Sources retrieved: dining_the_ridgeway_cafe.txt, housing_morrow_house_noise.txt, money_jobs.txt, transit_shuttle.txt

```
Based on the provided documents, the campus shuttle runs a loop every 20 minutes from 7 am to 11 pm on weekdays, and every 40 minutes on weekends. The published timetable is optimistic by about five minutes in the morning and accurate for the rest of the day, and the shuttle is free with a student ID. 

Source: `transit_shuttle.txt`
```

### What do students say about the accessibility & operating hours of the      transit shuttle on campus? — run 2

- Best distance: 0.3749 (passed the gate)
- Sources retrieved: dining_the_ridgeway_cafe.txt, housing_morrow_house_noise.txt, money_jobs.txt, transit_shuttle.txt

```
Based on the provided documents, the campus shuttle runs a loop every 20 minutes from 7 am to 11 pm on weekdays, and every 40 minutes on weekends. The published timetable is optimistic by about five minutes in the morning and is accurate the rest of the day. Additionally, the shuttle is free with a student ID. 
(Source: `transit_shuttle.txt`)
```

### What do students say about the accessibility & operating hours of the      transit shuttle on campus? — run 3

- Best distance: 0.3749 (passed the gate)
- Sources retrieved: dining_the_ridgeway_cafe.txt, housing_morrow_house_noise.txt, money_jobs.txt, transit_shuttle.txt

```
The campus shuttle runs a loop every 20 minutes from 7am to 11pm on weekdays and every 40 minutes on weekends. It is free with a student ID. (Source: transit_shuttle.txt)
```

### What advice do students most commonly leave when it comes to registering for      your courses & picking your adviser? — run 1

- Best distance: 0.5460 (passed the gate)
- Sources retrieved: admin_declaring_a_major.txt, advising_registration.txt, money_textbooks.txt, orientation_what_matters.txt

```
You need to have your adviser hold lifted before you can register, and since advisers get very busy the week before registration opens, you should book an appointment two weeks out. Additionally, registration times are staggered by credit hours, and popular courses tend to fill up within the first two days. 

Source: `advising_registration.txt`
```

### What advice do students most commonly leave when it comes to registering for      your courses & picking your adviser? — run 2

- Best distance: 0.5460 (passed the gate)
- Sources retrieved: admin_declaring_a_major.txt, advising_registration.txt, money_textbooks.txt, orientation_what_matters.txt

```
Students advise that you need your adviser hold lifted before registering, and because advisers get busy in the week before registration opens, you should book two weeks out. Additionally, registration times are staggered by credit hours, and popular courses fill up in the first two days. 

Source: `advising_registration.txt`
```

### What advice do students most commonly leave when it comes to registering for      your courses & picking your adviser? — run 3

- Best distance: 0.5460 (passed the gate)
- Sources retrieved: admin_declaring_a_major.txt, advising_registration.txt, money_textbooks.txt, orientation_what_matters.txt

```
Based on the provided documents, students advise that you need your adviser hold lifted before registering, and you should book your adviser two weeks out because they get very busy the week before registration opens. Registration times are staggered by credit hours, and popular courses tend to fill up in the first two days. 

Source: `advising_registration.txt`
```

### What do students say about the overall dining experience at campus, when     it comes to dining halls on campus, cost of meals plans, and accessibility of dining dollars? — run 1

- Best distance: 0.4335 (passed the gate)
- Sources retrieved: admin_dining_dollars.txt, dining_pellew_dining_hall.txt, dining_pellew_dining_hall_followup.txt, money_jobs.txt

```
Based on the provided documents:

* **Dining halls:** Students note that Pellew Dining Hall is the furthest hall from anywhere, located next to the athletics centre, and has peak wait times of 12 to 18 minutes. Going before 11:45 helps avoid the wait (*dining_pellew_dining_hall_followup.txt*). It costs one meal swipe or $11.75 cash (*dining_pellew_dining_hall.txt*).
* **Dining dollars:** Dining dollars roll over from the autumn semester to the spring semester, but whatever is left in May disappears and does not roll over to the following autumn (*admin_dining_dollars.txt*). 

*(Note: The provided documents do not contain information about the overall cost of meal plans beyond the single-meal cost at Pellew).*
```

### What do students say about the overall dining experience at campus, when     it comes to dining halls on campus, cost of meals plans, and accessibility of dining dollars? — run 2

- Best distance: 0.4335 (passed the gate)
- Sources retrieved: admin_dining_dollars.txt, dining_pellew_dining_hall.txt, dining_pellew_dining_hall_followup.txt, money_jobs.txt

```
Based on the provided documents, dining dollars (declining balance) roll over from the autumn semester to the spring semester, but whatever is left in May disappears and does not roll over to the following autumn (*admin_dining_dollars.txt*). Pellew Dining Hall costs one meal swipe or $11.75 cash, has a peak wait time of 12 to 18 minutes, and is the furthest dining hall from anywhere, located next to the athletics centre (*dining_pellew_dining_hall.txt* and *dining_pellew_dining_hall_followup.txt*).
```

### What do students say about the overall dining experience at campus, when     it comes to dining halls on campus, cost of meals plans, and accessibility of dining dollars? — run 3

- Best distance: 0.4335 (passed the gate)
- Sources retrieved: admin_dining_dollars.txt, dining_pellew_dining_hall.txt, dining_pellew_dining_hall_followup.txt, money_jobs.txt

```
Based on the provided documents:

* **Dining halls:** Students note that Pellew Dining Hall is the furthest hall from anywhere, located next to the athletics centre, and has peak wait times of 12 to 18 minutes. Going before 11:45 helps avoid the wait. (*dining_pellew_dining_hall_followup.txt* and *dining_pellew_dining_hall.txt*)
* **Cost of meal plans:** Pellew Dining Hall costs one meal swipe or $11.75 cash. (*dining_pellew_dining_hall.txt*)
* **Dining dollars:** Declining balance (dining dollars) rolls over from the autumn semester to the spring, but any remaining balance in May disappears and does not roll over to the following autumn. (*admin_dining_dollars.txt*)
```
