# Q3 – FFA, Vom Film zum Kinoerlebnis (2026)

Main time series of the project: cinema tickets in Germany per year, 2001–2025.

## Source

- Publisher: FFA (Filmförderungsanstalt, German Federal Film Board)
- Publication: [Vom Film zum Kinoerlebnis (PDF)](https://www.ffa.de/files/dokumentenverwaltung/studien%20mafo/2026/Vom_Film_zum_Kinoerlebnis_Zahlen-Daten-Fakten_FKM_2026.pdf), slides 9 and 13
- Licence: use and publication with permission from the FFA, with source ([permission](../../docs/sources/ffa_permission.md))
- How to cite: Source: Filmförderungsanstalt (FFA), Vom Film zum Kinoerlebnis (2026)

## Data

| | File | Content |
|---|---|---|
| Raw | `data/raw/ffa/ffa_tickets_total_arthouse_2001_2025.csv` | Tickets in all cinemas and in arthouse cinemas, 6 columns |
| Clean | `data/processed/q3_ffa_tickets.csv` | `year`, `tickets_total_million`, 25 rows (2001–2025) |

## Used for

- Sub-question 1: cinema attendance per person and breaks in the trend (with Q6 population)
- Sub-question 5: cinema attendance before and after the launch of Netflix and Amazon Prime Video (2014)

## Steps

| Step | File | What I did | Status |
|---|---|---|---|
| 1 | `01_explore.ipynb` | Looked at the raw data: columns, years, values; wrote first observations and questions for the analysis | done |
| 2 | `02_clean.ipynb` | Removed 4 columns that are not needed, checked for missing values, saved the clean table | done |
| 2 | [`scripts/q3_clean.py`](../../scripts/q3_clean.py) | Same cleaning steps as a script. Run from the main folder: `python scripts/q3_clean.py` | done |

## Known issues

- Values are taken from chart labels in the PDF, so they are rounded to 0.1 million.
- 2020 and 2021: cinemas were closed for months because of COVID-19.

## Later

- `data/raw/ffa/ffa_german_market_share_2001_2025.csv` (market share of German films) will be cleaned later, so it can be combined with Letterboxd.