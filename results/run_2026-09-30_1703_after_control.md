# Run log — after_control

- Produced by: `run_eval.py::main`
- Retrieval: `store.py::search`, chunks from `chunker.py::split_documents`
- Corpus: `campus_life` (index variant `default`)
- top-k: 5 · relevance cutoff: 0.6
- Runs per question: 3, caching off
- When: 2026-09-30 17:03

This table is one row per QUESTION. The run log your README asks for is
one row per CRITERION, so aggregate these into it — criterion 1 is how many
of your questions had the answer in the retrieved chunks, and so on.

| Question | Run 1 | Run 2 | Run 3 |
|---|---|---|---|
| What do students say about the quality & selection of food at      the Kestral Commons during lunch? | pass | pass | pass |
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
- Sources retrieved: dining_kestrel_commons.txt, dining_kestrel_commons_followup.txt, dining_north_kitchen_followup.txt, dining_the_ridgeway_cafe_followup.txt

```
Students state that the stir-fry station is made to order and is worth going for, but the salad bar wilts after 1:30. 

Source: `dining_kestrel_commons.txt`
```

### What do students say about the quality & selection of food at      the Kestral Commons during lunch? — run 2

- Best distance: 0.4519 (passed the gate)
- Sources retrieved: dining_kestrel_commons.txt, dining_kestrel_commons_followup.txt, dining_north_kitchen_followup.txt, dining_the_ridgeway_cafe_followup.txt

```
Students state that the thing worth going for at Kestrel Commons is the stir-fry station, which is made to order, but they also mention that the salad bar wilts after 1:30. 

Source: `dining_kestrel_commons.txt` (and `dining_kestrel_commons_followup.txt`)
```

### What do students say about the quality & selection of food at      the Kestral Commons during lunch? — run 3

- Best distance: 0.4519 (passed the gate)
- Sources retrieved: dining_kestrel_commons.txt, dining_kestrel_commons_followup.txt, dining_north_kitchen_followup.txt, dining_the_ridgeway_cafe_followup.txt

```
Based on the documents, students state that the salad bar wilts after 1:30, and they recommend the made-to-order stir-fry station as the thing worth going for. 

Source: `dining_kestrel_commons.txt` (and `dining_kestrel_commons_followup.txt`)
```

### What do students say about the amount of study time needed outside of class     each week for computer science courses? — run 1

- Best distance: 0.4077 (passed the gate)
- Sources retrieved: course_cs_210.txt, course_cs_210_workload.txt, course_cs_340.txt, course_econ_101_workload.txt, course_stat_150_workload.txt

```
For CS 210 Data Structures, students can expect 8 to 10 hours a week outside of class (source: `course_cs_210_workload.txt` and `course_cs_210.txt`). For CS 340 Databases, students can expect 6 hours a week early on, increasing to 15 hours a week in the last three weeks when the project lands (source: `course_cs_340.txt`).
```

### What do students say about the amount of study time needed outside of class     each week for computer science courses? — run 2

- Best distance: 0.4077 (passed the gate)
- Sources retrieved: course_cs_210.txt, course_cs_210_workload.txt, course_cs_340.txt, course_econ_101_workload.txt, course_stat_150_workload.txt

```
For CS 210 Data Structures, students can expect 8 to 10 hours a week outside of class (from `course_cs_210_workload.txt` and `course_cs_210.txt`). 

For CS 340 Databases, students should expect about 6 hours a week early on, increasing to 15 hours a week in the last three weeks when the project lands (from `course_cs_340.txt`).
```

### What do students say about the amount of study time needed outside of class     each week for computer science courses? — run 3

- Best distance: 0.4077 (passed the gate)
- Sources retrieved: course_cs_210.txt, course_cs_210_workload.txt, course_cs_340.txt, course_econ_101_workload.txt, course_stat_150_workload.txt

```
For CS 210 Data Structures, students can expect 8 to 10 hours a week outside of class (source: `course_cs_210_workload.txt` and `course_cs_210.txt`). For CS 340 Databases, students can expect about 6 hours a week early on, increasing to 15 hours a week in the last three weeks when the project lands (source: `course_cs_340.txt`).
```

### What do students say about the accessibility & operating hours of the      transit shuttle on campus? — run 1

- Best distance: 0.3749 (passed the gate)
- Sources retrieved: housing_aldridge_hall_noise.txt, study_library_hours.txt, transit_shuttle.txt, transit_walking.txt

```
Based on the documents, the campus shuttle runs a loop every 20 minutes from 7am to 11pm on weekdays and every 40 minutes on weekends, and it is free with a student ID. Its published timetable is optimistic by about five minutes in the morning and accurate the rest of the day. 

Source: *transit_shuttle.txt*
```

### What do students say about the accessibility & operating hours of the      transit shuttle on campus? — run 2

- Best distance: 0.3749 (passed the gate)
- Sources retrieved: housing_aldridge_hall_noise.txt, study_library_hours.txt, transit_shuttle.txt, transit_walking.txt

```
Based on the provided documents, the campus shuttle runs a loop every 20 minutes from 7am to 11pm on weekdays and every 40 minutes on weekends. It is free with a student ID, and the stop outside Fenwick Court gets skipped when the driver is behind. Additionally, the published timetable is optimistic by about five minutes in the morning and accurate the rest of the day. 

Source: *transit_shuttle.txt*
```

### What do students say about the accessibility & operating hours of the      transit shuttle on campus? — run 3

- Best distance: 0.3749 (passed the gate)
- Sources retrieved: housing_aldridge_hall_noise.txt, study_library_hours.txt, transit_shuttle.txt, transit_walking.txt

```
Based on the provided documents, the campus shuttle runs a loop every 20 minutes from 7 am to 11 pm on weekdays and every 40 minutes on weekends. It is free with a student ID, and the published timetable is optimistic by about five minutes in the morning and accurate the rest of the day. Additionally, the stop outside Fenwick Court gets skipped when the driver is behind. 

Source: *transit_shuttle.txt*
```

### What advice do students most commonly leave when it comes to registering for      your courses & picking your adviser? — run 1

- Best distance: 0.5460 (passed the gate)
- Sources retrieved: admin_declaring_a_major.txt, admin_wifi_and_accounts.txt, advising_registration.txt, dining_verrill_street_grill.txt, money_textbooks.txt

```
Based on the provided documents, students advise booking an appointment with your adviser two weeks out because they get busy in the week before registration opens, and note that you need your adviser hold lifted before you can register. (Source: `advising_registration.txt`)
```

### What advice do students most commonly leave when it comes to registering for      your courses & picking your adviser? — run 2

- Best distance: 0.5460 (passed the gate)
- Sources retrieved: admin_declaring_a_major.txt, admin_wifi_and_accounts.txt, advising_registration.txt, dining_verrill_street_grill.txt, money_textbooks.txt

```
Students advise that you need your adviser hold lifted before you can register, and since advisers get busy in the week before registration opens, you should book two weeks out (*advising_registration.txt*). Additionally, registration times are staggered by credit hours, and popular courses fill up in the first two days (*advising_registration.txt*).
```

### What advice do students most commonly leave when it comes to registering for      your courses & picking your adviser? — run 3

- Best distance: 0.5460 (passed the gate)
- Sources retrieved: admin_declaring_a_major.txt, admin_wifi_and_accounts.txt, advising_registration.txt, dining_verrill_street_grill.txt, money_textbooks.txt

```
According to `advising_registration.txt`, students advise booking your adviser two weeks out because they get busy the week before registration, as you need your adviser hold lifted to register. Popular courses also fill up in the first two days.
```

### What do students say about the overall dining experience at campus, when     it comes to dining halls on campus, cost of meals plans, and accessibility of dining dollars? — run 1

- Best distance: 0.4335 (passed the gate)
- Sources retrieved: admin_dining_dollars.txt, admin_meal_plan_changes.txt, dining_pellew_dining_hall.txt, dining_verrill_street_grill.txt, money_jobs.txt

```
Based on the provided documents, Pellew Dining Hall costs one meal swipe or $11.75 in cash. (Source: dining_pellew_dining_hall.txt) Additionally, dining dollars (declining balance) roll over from the autumn semester to the spring semester, but whatever is left in May disappears and does not roll over to the following autumn. (Source: admin_dining_dollars.txt)
```

### What do students say about the overall dining experience at campus, when     it comes to dining halls on campus, cost of meals plans, and accessibility of dining dollars? — run 2

- Best distance: 0.4335 (passed the gate)
- Sources retrieved: admin_dining_dollars.txt, admin_meal_plan_changes.txt, dining_pellew_dining_hall.txt, dining_verrill_street_grill.txt, money_jobs.txt

```
Based on the provided documents, Pellew Dining Hall costs one meal swipe or $11.75 cash (from `dining_pellew_dining_hall.txt`). Meal plan tiers can be changed once within the first ten days of the semester, after which they are locked, with downgrades resulting in a refund and upgrades resulting in an immediate bill (from `admin_meal_plan_changes.txt`). Regarding dining dollars, declining balance funds roll over from autumn to spring, but any remaining balance in May disappears and does not roll over to the following autumn (from `admin_dining_dollars.txt`).
```

### What do students say about the overall dining experience at campus, when     it comes to dining halls on campus, cost of meals plans, and accessibility of dining dollars? — run 3

- Best distance: 0.4335 (passed the gate)
- Sources retrieved: admin_dining_dollars.txt, admin_meal_plan_changes.txt, dining_pellew_dining_hall.txt, dining_verrill_street_grill.txt, money_jobs.txt

```
Based on the provided documents, Pellew Dining Hall costs one meal swipe or $11.75 cash (*dining_pellew_dining_hall.txt*). Meal plan tiers can be changed once within the first ten days of the semester, after which they are locked (*admin_meal_plan_changes.txt*). Additionally, dining dollars roll over from the autumn semester to the spring semester, but any remaining balance in May disappears and does not roll over to the following autumn (*admin_dining_dollars.txt*).
```
