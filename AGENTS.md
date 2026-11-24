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

### Traps

**FFA files**

- The numbers were copied by hand from charts in PDFs and are **rounded** (27 % instead of 27.4 %).
- Separator `,`, decimal point `.`. All files except `ffa_cinemas_arthouse_2016_2025.csv` have the columns `source_id` and `source`.
- Empty cells in `ffa_spending_cinema_homevideo_2003_2025.csv` mean the chart showed no value. They are missing, not 0.
- **Breaks:** the definition of arthouse cinemas changed in 2009 (column

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