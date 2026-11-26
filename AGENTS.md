# AGENTS.md

Instructions for AI coding agents (GitHub Copilot, Claude, ChatGPT and others) in this repository.

## Project

Group project for DIS 3.3 Data Integration (TH Köln, winter semester 2026/27): **Cinema Visits in Germany (2001–2025)**.
Main question: How will movie attendance in Germany change by 2026? The sub-questions, the folder structure and the plan are in `README.md`.

## Setup and commands

We have no `requirements.txt` yet. Until then:

- Python 3, with the packages `pandas`, `matplotlib` and `jupyter`.
- Create and activate a virtual environment:
  - macOS: `python3 -m venv .venv` and `source .venv/bin/activate`
  - Windows: `python -m venv .venv` and `.venv\Scripts\activate.bat`
- Install the packages: `python -m pip install pandas matplotlib jupyter`
- Run each script from the main folder of the repository, e.g. `python scripts/q1_cinema_key_figures/q1_cleaning.py`.
- Open notebooks in VS Code or with `jupyter notebook`, and run them from top to bottom.
- Tests: none yet. When we add them, they run with `python -m pytest`.

## Documentation

- After every team meeting, we write a protocol in `docs/meetings/` (see `docs/meetings/README.md`).

## Data

Raw data lives in `data/raw/<source>/`, cleaned data in `data/processed/`. Every folder in `data/raw/` has a README with details; the full list of sources, limitations and licences is in `docs/sources/README.md`.
 
### Sources and licences
 
| ID | Source | Folder | Licence | How to cite |
|---|---|---|---|---|
| Q1, Q2, Q3, Q8 | FFA (Filmförderungsanstalt): Das Kinojahr 2025; Kinobesucher\*innen 2025; Vom Film zum Kinoerlebnis (2026); cinema table sent by email | `data/raw/ffa/` | No open licence. The FFA allowed us to use, combine and publish its numbers with the source (`docs/sources/ffa_permission.md`). Never upload the FFA PDFs or pictures. | Source: Filmförderungsanstalt (FFA), followed by the title of the report, e.g. Das Kinojahr 2025 |
| Q6, Q7 | Destatis, GENESIS-Online tables 12411-0001 and 12411-0003 (population) | `data/raw/destatis/` | dl-de/by-2-0 | © Statistisches Bundesamt (Destatis), 2026 |
| – | Kaggle: Letterboxd Movie Rating; Top 500 Movies Ranked by IMDb, Rotten & Letterboxd | `data/raw/kaggle/` (links only) | CC BY 4.0; CC BY-NC-SA 4.0 (non-commercial, share alike) | Name the dataset, its author and the link |
 
### Units
 
- `year` is the key that joins all sources.
- Tickets: in **millions** in most FFA files (`tickets_total_million`), but as a **plain count** in `ffa_kinojahr_key_figures_2021_2025.csv` (`tickets`, `revenue_eur`). Check the column name before you combine.
- Money: `_million_eur` or `_eur`, as the column name says.
- Percentages are whole numbers from 0 to 100 (`_percent`), not shares from 0 to 1.
- Population (Destatis): number of people on 31 December of each year.
 
### Cleaned files (join these on `year`)
 
| File | Years | Key columns and units |
|---|---|---|
| `q1_ffa_kinojahr_key_figures_2021_2025_clean.csv` | 2021–2025 | `population_ffa` (the FFA's population), `tickets` (plain count), `revenue_eur`, `avg_ticket_price_eur`, `screens` |
| `q2_ffa_visitors_clean.csv` | 2003–2025 | spending in `_million_eur`; `cinema_visitors_million`; `visits_per_person` (per cinema visitor, not per inhabitant); age and sex in `_percent`; `tickets_panel_million` (ticket base of the panel survey, not the official count); `reach_survey_population` |
| `q3_ffa_tickets.csv` | 2001–2025 | `tickets_total_million`: the official number of tickets |
| `q6_destatis_population.csv` | 2001–2025 | `population`: Destatis, people on 31 December |
 
`year` is an integer in every file. Some names differ from the raw files, e.g. `tickets_base_million` (raw) is `tickets_panel_million` (cleaned).
 
### Traps
 
**FFA files**
 
- The numbers were copied by hand from charts in PDFs and are **rounded** (27 % instead of 27.4 %).
- Separator `,`, decimal point `.`. All files except `ffa_cinemas_arthouse_2016_2025.csv` have the columns `source_id` and `source`.
- Empty cells in `ffa_spending_cinema_homevideo_2003_2025.csv` mean the chart showed no value. They are missing, not 0.
- **Breaks:** the definition of arthouse cinemas changed in 2009 (column `arthouse_definition`). From 2025, cinemas are counted without drive-ins, open-air cinemas and festivals. In Q2, only German citizens aged 10+ were counted until 2018; from 2019, everyone aged 10+ living in Germany.
- **COVID-19:** cinemas were closed for months in 2020 and 2021. Mark these years; do not treat them as normal years.
 
**Destatis files**
 
- Separator `;`, encoding **UTF-8 with BOM** (read with `encoding="utf-8-sig"`).
- The first lines are a title, the last lines are notes. Read only the rows that start with a date such as `31.12.2023` (see `scripts/q6_destatis_population/`).
- Columns are German: `Anzahl` = number, `Insgesamt` = total, `männlich`/`weiblich` = male/female. `e` = final value, not a number.
- **Breaks:** until 1989 only West Germany (jump in 1990); new census bases from 2011 and from 2022.
 
**Two different population numbers**
 
- The FFA uses its own population (`population_ffa`), which differs from Destatis (2023: FFA 84,607,016, Destatis 83,456,045). Do not mix them in one calculation. Say which one you used.
 
**Kaggle**
 
- The files are too large for GitHub. Download them from Kaggle and never commit them. The data ends around 2021.
 
**Cleaned files**
 
- `visits_per_person` (Q2) is per cinema visitor: `cinema_visitors_million` × `visits_per_person` ≈ `tickets_panel_million`. For tickets per inhabitant, divide `tickets_total_million` (Q3) by `population` (Q6).
- For per-person values, use the Destatis `population` (Q6, 2001–2025), not `population_ffa` (Q1, only 2021–2025). The two differ by about 1.15 million in 2022 and 2023, because Destatis recalculated its numbers after the census of 2022.
- In `q2_ffa_visitors_clean.csv`, empty cells mean "not reported", not 0. `reach_survey_population` is empty before 2015, `german_citizens` until 2018 and `all_residents` from 2019, so reach and visitor numbers are not comparable across 2018/2019.


## Rules for AI Agents

### 1. Raw Data Protection
- Never modify, delete or overwrite files in `data/raw/`.
- Treat all original datasets as read-only.
- Do not commit raw datasets to Git.
- Save cleaned and transformed data separately in `data/processed/`.

### 2. Data Quality
- Do not silently remove or fill missing values.
- Report missing values, duplicates and unexpected data types.
- Check the number of rows before and after filtering or merging.
- Preserve the original units and document all conversions.
- Do not change column names without explaining the changes.
- Check that datasets use compatible years, country names and units before merging.
- Do not treat missing values as zero unless this is explicitly justified.

### 3. Privacy and Data Sources
- Never include personal or sensitive information in AI prompts.
- Do not invent data sources, URLs or licence information.
- Respect the licences and usage conditions of all datasets.
- Ask before using data from a source with unclear permissions.
- Do not download or scrape data from IMDb, Letterboxd or similar platforms without checking their terms of use and permissions.

### 4. Code and Testing
- Do not modify existing tests without permission.
- Run tests after code changes and report the results.
- Do not install additional Python packages without approval.
- Make only the requested changes and avoid unnecessary modifications.
- Explain planned changes before implementing them.

### 5. AI Usage and Human Review
- Document every use of AI in `AI_USAGE.md`.
- Record the AI tool, model, purpose and important prompts.
- Document which suggestions were accepted, modified or rejected.
- Do not commit or push changes without human approval.
- All AI-generated code and results must be reviewed by a team member.