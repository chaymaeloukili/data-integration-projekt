# FFA data

Data from the FFA (Filmförderungsanstalt, German Federal Film Board).
The FFA allowed the use and publication of their numbers with the source, see [ffa_permission.md](../../../docs/sources/ffa_permission.md).
The original FFA files (PDFs, PowerPoint) are not uploaded.

The numbers were copied from the FFA files into CSV files by Chaymae Loukili.
Every file has two extra columns:

- `source_id`: number of the source in the [source overview](../../../docs/sources/README.md)
- `source`: publication and page

Separator: `,` (comma). Decimal point: `.`

## Files

| File | Source | Content | Years |
|---|---|---|---|
| `ffa_cinemas_arthouse_2016_2025.csv` | Q8 (PowerPoint, sent by the FFA on 27.10.2026) | Number of cinemas and tickets, all cinemas and arthouse cinemas | 2016–2025 |
| `ffa_kinojahr_key_figures_2021_2025.csv` | Q1, Das Kinojahr 2025, p. 6, 8, 9 | Tickets, revenue, ticket price, cinemas, screens, seats, German films, 3D | 2021–2025 |
| `ffa_visitors_age_gender_2021_2025.csv` | Q2, Kinobesucher\*innen 2025, p. 12 | Share of tickets by sex and age group | 2021–2025 |
| `ffa_visitors_reach_2015_2025.csv` | Q2, Kinobesucher\*innen 2025, p. 16, 58 | Number of cinema visitors, reach, visits per person, home video users | 2015–2025 |
| `ffa_spending_cinema_homevideo_2003_2025.csv` | Q2, Kinobesucher\*innen 2025, p. 60 | Spending on cinema, DVD/Blu-ray, download/rental (EST/TVoD) and streaming subscriptions (SVoD) | 2003–2025 |
| `ffa_cinema_svod_subscribers_2025.csv` | Q2, Kinobesucher\*innen 2025, p. 59 | Cinema use of streaming subscribers compared to the population | 2025 |
| `ffa_tickets_total_arthouse_2001_2025.csv` | Q3, Vom Film zum Kinoerlebnis, slide 9 | Tickets in all cinemas and in arthouse cinemas | 2001–2025 |
| `ffa_german_market_share_2001_2025.csv` | Q3, Vom Film zum Kinoerlebnis, slide 13 | Market share of German films | 2001–2025 |

## Important notes

- **Rounded values:** Many numbers in the FFA reports are only shown as labels in charts. They are rounded (for example 27 % instead of 27.4 %).
- **Empty cells:** In `ffa_spending_cinema_homevideo_2003_2025.csv`, a cell is empty when the chart shows no value for that year.
- **Number of cinemas 2025:** From 2025, the FFA counts cinemas without drive-in cinemas, open-air cinemas and festivals. The number of cinemas in 2025 is not directly comparable with earlier years.
- **Arthouse cinemas:** The FFA changed the definition of "arthouse cinema" (Programmkino) in 2009. Years before 2009 are not comparable with later years (see column `arthouse_definition`).
- **Visitor data (Q2):** Based on a panel of YouGov (about 12,000 people for cinema, about 93,500 for home video). Until 2018 only German citizens aged 10+ were counted, from 2019 everyone aged 10+ living in Germany.
- **Population:** The FFA uses different population numbers than Destatis (see [data/raw/destatis](../destatis/README.md)).
- **COVID-19:** Cinemas were closed for months in 2020 and 2021.

## How to cite

- Source: Filmförderungsanstalt (FFA), Das Kinojahr 2025
- Source: Filmförderungsanstalt (FFA), Kinobesucher\*innen 2025
- Source: Filmförderungsanstalt (FFA), Vom Film zum Kinoerlebnis (2026)
