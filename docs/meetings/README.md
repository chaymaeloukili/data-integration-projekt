## Meeting 14.11.2026

### Labs

- The labs are done in pairs:
  - Chaymae and Ülkü: Monday, 16.11.2026
  - Hafssa and Aqsa: Tuesday, 17.11.2026
- The last task of the lab (group task) is done together on **24.11.2026** (meeting at the university, from 15:00).

### Check-ups

| Date | Time | Where |
|---|---|---|
| Thursday, 19.11.2026 | 14:00 | online, short check-up |
| Tuesday, 24.11.2026 | 15:00 | at the university, check-up and group lab task |

### Cleaning

- The data is cleaned with **Python scripts** (`scripts/`). The steps are then transferred to **Jupyter notebooks** (`notebooks/`) with notes that explain each step. This was recommended by the lecturer.
- Cleaning deadlines:

| Source | Responsible | Deadline | Status |
|---|---|---|---|
| Q6 Destatis, population | Hafssa | 15.11.2026 | almost done |
| Q1 FFA, Das Kinojahr + Letterboxd | Ülkü | 20.11.2026 | in progress |
| Q3 FFA, Vom Film zum Kinoerlebnis | Chaymae | 20.11.2026 | in progress |
| Q2 FFA, Kinobesucher\*innen | Aqsa | 22.11.2026 | in progress |

### Next step: data integration

After her cleaning, Hafssa looks into how to combine the cleaned data technically until the next meeting (24.11.2026):

- How do we join the datasets correctly (by `year`)?
- Which workflow do we all use, and how do we use Git and Bash for it?
- Goal: everyone works the same way, so we can all explain it and do not get confused.

Which data is combined and which research question it answers is already clear (see [README](../../README.md)).

### Documentation

- If someone changes something (e.g. in a README) that the others do not know about, they write a short explanation in the side notes in `docs/`.

### Tasks per person

| Person | Task | Deadline |
|---|---|---|
| Hafssa | Clean Q6 (Destatis, population): script + notebook → `data/processed/` | 15.11.2026 |
| Hafssa | Find out how to combine the cleaned data (join by `year`, workflow with Git and Bash) and present it | 24.11.2026 |
| Hafssa | Labs together with Aqsa | Tuesday, 17.11.2026 |
| Ülkü | Clean Q1 (FFA, Das Kinojahr) + Letterboxd: script + notebook → `data/processed/` | 20.11.2026 |
| Ülkü | Labs together with Chaymae | Monday, 16.11.2026 |
| Chaymae | Clean Q3 (FFA, Vom Film zum Kinoerlebnis): script + notebook → `data/processed/` | 20.11.2026 |
| Chaymae | Labs together with Ülkü | Monday, 16.11.2026 |
| Aqsa | Clean Q2 (FFA, Kinobesucher\*innen): script + notebook → `data/processed/` | 22.11.2026 |
| Aqsa | Labs together with Hafssa | Tuesday, 17.11.2026 |

### Tasks for everyone

| Task | Deadline |
|---|---|
| Online check-up | Thursday, 19.11.2026, 14:00 |
| Meeting at the university: check-up and group lab task | Tuesday, 24.11.2026, 15:00 |
| Write changes that others do not know about in the side notes in `docs/` | always |
| Document AI use in your own table in `AI_USAGE.md` | always |

---
# Meeting at 08.11.2026
## Research Question:
The research question has been formulated:
**How will movie attendance in Germany change by 2026?**

- Possible sub-questions have been discussed.
 
| Number | Sub-questions |
| :----- | :------------ |
| 1 | How did movie theater attendance per person change from 2001 to 2025, and where are the breaks in the trend (e.g., 2014, 2020)? Q3 + Q6 + Timeline|
| 2 | Is streaming replacing movie theaters, or are both growing side by side? How have spending on movie theaters and streaming changed from 2003 to 2025? Q2 |
| 3 | Who is returning to movie theaters after the pandemic? How are age groups and ticket prices changing from 2021 to 2025? Q2 + Q1 |
| 4 | Which movies and genres are particularly successful in Germany, and has this changed over the years? Q1 (Top 10) + Letterboxd/Wikidata |
| 5 | Compare movie theater attendance in 2014 with that from 2014–2019—that is, before and after the launch of Amazon Prime and Netflix. We’re deliberately excluding the COVID-19 years from this comparison. |


## Source Distribution (Deadlines for Cleaning):
- Aqsa; Q2 (till 22.11)
- Hafssa; Q6 (till 15.11)
- Ülkü; Q1 (till 20.11) + Letterboxd source
- Chaymae; Q3 (till 20.11)

***Checkup Date: 14.11 at 11 am***

- All of the cleaned Data has to be uploaded to [processed](https://github.com/chaymaeloukili/data-integration-projekt/tree/main/data/processed)
