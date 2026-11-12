# Cinema Visits in Germany (2001–2025)

Group project for the module DIS 3.3 Data Integration (Timo Breuer), TH Köln, winter semester 2026/27.

> **Status:** Work in progress. The base datasets are being explored and cleaned.

## Topic

We look at how cinema visits in Germany have changed since 2001: the rise of streaming, the COVID-19 closures and the recovery afterwards. We combine data on cinema visits, streaming, population and films by year.

## Research question

**How has cinema attendance in Germany changed between 2001 and 2025, and what role do streaming and the COVID-19 pandemic play?**

| # | Sub-question | Data |
|---|---|---|
| 1 | How did cinema attendance per person change from 2001 to 2025, and where are the breaks in the trend (e.g. 2014, 2020)? | Q3, Q6, timeline |
| 2 | Is streaming replacing cinemas, or are both growing side by side? How did spending on cinema and streaming change from 2003 to 2025? | Q2 |
| 3 | Who is returning to cinemas after the pandemic? How did age groups and ticket prices change from 2021 to 2025? | Q2, Q1 |
| 4 | Which films and genres are particularly successful in Germany, and has this changed over the years? | Q1 (Top 10), Letterboxd/Wikidata |
| 5 | How did cinema attendance change before and after the launch of Netflix and Amazon Prime Video in Germany (2014)? The COVID-19 years are excluded. | Q3, Q6 |

## Data sources

| ID | Source | Publisher | Years | Licence |
|---|---|---|---|---|
| Q1 | Das Kinojahr 2025 | FFA (German Federal Film Board) | 2021–2025 | Permission from the FFA |
| Q2 | Kinobesucher\*innen 2025 | FFA | 2003–2025 | Permission from the FFA |
| Q3 | Vom Film zum Kinoerlebnis (2026) | FFA | 2001–2025 | Permission from the FFA |
| Q6 | Population, Germany (12411-0001) | Destatis | 1950–2025 | dl-de/by-2-0 |
| – | Letterboxd Movie Rating | Kaggle | until approx. 2021 | CC BY 4.0 |
| – | Timeline of events | various | 2001–2025 | see sources |

The FFA allowed us to use and publish their numbers with the source ([permission](docs/sources/ffa_permission.md)). The FFA PDFs are not uploaded.
All sources, limitations and possible bias: [docs/sources](docs/sources/README.md)

## Plan

| Until | Step | Milestone |
|---|---|---|
| 13.11.2026 | Topic, sources, licences and research questions | Milestone 1: Roadmap |
| end of November | Explore and clean the base datasets → `data/processed/` | |
| 18.12.2026 | Combine the data by year, first pipeline, documentation | Milestone 2: Dataset |
| January 2027 | Analysis, visualisations, notebook | |
| 22.01.2027, 23:59 | Last commit | Repository deadline |
| 25.01.2027 | Presentation with running notebook | Milestone 3: Presentation |

## Team

| Name | GitHub |
|---|---|
| Ülkü Arslan | @ulkuarsl |
| Hafssa Zainou | @hafssazainou |
| Aqsa Shaikh | @ashaikhh |
| Chaymae Loukili | @chaymaeloukili |

## Repository structure

| Folder | Content |
|---|---|
| `docs/sources/` | All checked sources with licences and limitations |
| `docs/meetings/` | Meeting notes and task distribution |
| `data/raw/` | Original data (never changed) |
| `data/processed/` | Cleaned and combined data |
| `scripts/`, `notebooks/` | Code for cleaning and analysis |
| `team/` | Personal work folders |

## Use of AI

We document every use of AI tools in [AI_USAGE.md](AI_USAGE.md).

## How to get the data

The raw data is not in this repository. The FFA reports are PDFs from [ffa.de](https://www.ffa.de/broschueren.html), and the population data is a CSV from [GENESIS-Online](https://genesis.destatis.de) (table 12411-0001). Download dates and details are in `docs/sources/`.

## Team rules

- Nobody pushes to `main`. Every change comes as a pull request on its own branch.
- A teammate reviews every pull request before it is merged.
- We write commit messages that say what changed and why.
- Every branch starts from an issue and is named `feature/<issue number>-<topic>`, e.g. `feature/5-branch-naming`. The pull request closes the issue with `Closes #<number>`.
