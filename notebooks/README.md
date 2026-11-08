# Notebooks

Jupyter notebooks for the project. The work is done in 4 steps:

| Step | Notebook | What happens | Where |
|---|---|---|---|
| 1 | `01_explore.ipynb` | Look at the raw data: columns, years, units, missing values, problems | one folder per source |
| 2 | `02_clean.ipynb` | Clean the data and save it to `data/processed/` | one folder per source |
| 3 | `03_analysis.ipynb` | Combine all cleaned data by `year` and answer the research questions | `combined/` |
| 4 | `04_visualisation.ipynb` | Charts for the results and the presentation | `combined/` |

> **Current status:** Steps 1 and 2 (explore and clean) are in progress.

## Folders

| Folder | Source | Raw data | Cleaned data |
|---|---|---|---|
| [q1_ffa_kinojahr](q1_ffa_kinojahr/) | Q1 FFA, Das Kinojahr 2025 | `data/raw/ffa/` | `data/processed/q1_ffa_kinojahr.csv` |
| [q2_ffa_visitors](q2_ffa_visitors/) | Q2 FFA, Kinobesucher\*innen 2025 | `data/raw/ffa/` | `data/processed/q2_ffa_visitors.csv` |
| [q3_ffa_tickets](q3_ffa_tickets/) | Q3 FFA, Vom Film zum Kinoerlebnis | `data/raw/ffa/` | `data/processed/q3_ffa_tickets.csv` |
| [q6_destatis_population](q6_destatis_population/) | Q6 Destatis, Population | `data/raw/destatis/` | `data/processed/q6_destatis_population.csv` |
| letterboxd | Kaggle, Letterboxd Movie Rating (later) | `data/raw/kaggle/` | `data/processed/letterboxd.csv` |
| [combined](combined/) | All sources combined | `data/processed/` | – |

## Rules

- Never change files in `data/raw/`.
- The year column is called `year` in every cleaned file.
- Column names: English, lower case, with underscore.
- Write short notes in the notebook: what you changed and why.
