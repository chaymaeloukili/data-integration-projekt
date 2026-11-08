
# Q3 – FFA, Vom Film zum Kinoerlebnis (2026)

Main time series of the project: cinema tickets in Germany per year, 2001–2025.

## Source

- Publisher: FFA (Filmförderungsanstalt, German Federal Film Board)
- Publication: [Vom Film zum Kinoerlebnis (PDF)](https://www.ffa.de/files/dokumentenverwaltung/studien%20mafo/2026/Vom_Film_zum_Kinoerlebnis_Zahlen-Daten-Fakten_FKM_2026.pdf), slides 9 and 13
- Licence: use and publication with permission from the FFA, with source ([permission](../../docs/sources/ffa_permission.md))
- How to cite: Source: Filmförderungsanstalt (FFA), Vom Film zum Kinoerlebnis (2026)

## Data

| Raw data | Content | Years |
|---|---|---|
| `data/raw/ffa/ffa_tickets_total_arthouse_2001_2025.csv` | Tickets in all cinemas and in arthouse cinemas, in million | 2001–2025 |
| `data/raw/ffa/ffa_german_market_share_2001_2025.csv` | Market share of German films, in percent | 2001–2025 |

Cleaned data: `data/processed/q3_ffa_tickets.csv`

## Used for

- Sub-question 1: cinema attendance per person and breaks in the trend (with Q6 population)
- Sub-question 4: success of German films over the years
- Sub-question 5: cinema attendance before and after the launch of Netflix and Amazon Prime Video (2014)

## Steps

| Step | Notebook | What I do | Status |
|---|---|---|---|
| 1 | `01_explore.ipynb` | Look at the data: columns, data types, years, units, missing values; compare some values with the PDF | in progress |
| 2 | `02_clean.ipynb` | Clean the data and combine both files into one table by `year`; save to `data/processed/` | open |

## Known issues

- Values are taken from chart labels in the PDF, so they are rounded (tickets to 0.1 million, market share to whole percent).
- The FFA changed the definition of arthouse cinemas in 2009. Arthouse values before 2009 are not directly comparable (column `arthouse_definition`).
- 2020 and 2021: cinemas were closed for months because of COVID-19.
