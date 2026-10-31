# Sources

This page lists all checked sources for the project.
Sources found and checked by Chaymae Loukili.
Last update: 31.10.2026

**Checked** means: the original source was opened and the content, years, format and licence were checked.

## Overview

| ID | Source | Publisher | Years | Format | Licence | Status |
|---|---|---|---|---|---|---|
| Q1 | [Das Kinojahr](https://www.ffa.de/broschueren.html) (The Cinema Year, annual report) | FFA (German Federal Film Board) | 2000–2025 | PDF | Permission from FFA | checked |
| Q2 | [Kinobesucher\*innen 2025](https://www.ffa.de/files/dokumentenverwaltung/studien%20mafo/2026/FFA_Kinobesucher_innen_2025.pdf) (Cinema visitors 2025) | FFA | 2025, some charts from 2015 | PDF | Permission from FFA | checked |
| Q3 | [Vom Film zum Kinoerlebnis](https://www.ffa.de/files/dokumentenverwaltung/studien%20mafo/2026/Vom_Film_zum_Kinoerlebnis_Zahlen-Daten-Fakten_FKM_2026.pdf) (From film to cinema experience) | FFA, survey by Ipsos | 2001–2025, survey 2026 | PDF | Permission from FFA | checked |
| Q4 | [Press release, 16.09.2026](https://www.ffa.de/pressemitteilungen-detailseite.html?meldung=kino-muss-heute-mehr-sein-als-ein-abspielort) | FFA | 2026 | Website | Quote only, with source | checked |
| Q5 | [Press release, 28.05.2026](https://www.ffa.de/pressemitteilungen-detailseite.html?meldung=ffa-studie-kinobesucherinnen-2025-mehr-publikum-wachstum-vor-allem-bei-aelteren) | FFA | 2025 | Website | Quote only, with source | checked |
| Q6 | [Population, Germany (12411-0001)](https://genesis.destatis.de/datenbank/online/statistic/12411/table/12411-0001/search/s/Rm9ydHNjaHJlaWJ1bmclMjBkZXMlMjBCZXYlQzMlQjZsa2VydW5nc3N0YW5kZXM%3D) | Destatis (Federal Statistical Office) | 1950–2025 | CSV | dl-de/by-2-0 | checked |
| Q7 | [Population, Germany, by sex (12411-0003)](https://genesis.destatis.de/datenbank/online/statistic/12411/table/12411-0003/search/s/Rm9ydHNjaHJlaWJ1bmclMjBkZXMlMjBCZXYlQzMlQjZsa2VydW5nc3N0YW5kZXM%3D) | Destatis | 1970–2025 | CSV | dl-de/by-2-0 | checked |
| Q8 | [Cinemas and arthouse cinemas 2016–2025](../../data/raw/ffa/ffa_cinemas_arthouse_2016_2025.csv) | FFA, sent by email on 27.10.2026 | 2016–2025 | PowerPoint, saved as CSV | Permission from FFA | checked |

## What is in each source

| ID | Content |
|---|---|
| Q1 | Tickets sold, box office, average ticket price, number of cinemas. Example: 91.9 million tickets in 2025. |
| Q2 | Who goes to the cinema: age, how often, cinema compared to streaming. |
| Q3 | Why people go to the cinema today. Tickets in all cinemas and in arthouse cinemas from 2001 to 2025 (as CSV in data/raw/ffa/). |
| Q4 | Short summary of Q3. Only for quotes. |
| Q5 | Short summary of Q2 (age groups). Only for quotes. |
| Q6 | Population of Germany per year (on 31 December). Needed to calculate tickets per person. |
| Q7 | Population per year by sex. Alternative to Q6. |
| Q8 | Number of cinemas and arthouse cinemas, tickets in all cinemas and in arthouse cinemas, per year. Same data as the chart in Q3, but as a table. |

## Limitations and possible bias

| ID | Limitation |
|---|---|
| Q1 | Numbers are only in PDFs. The years 2021–2025 were copied into a CSV (data/raw/ffa/). From 2025, the FFA counts cinemas without drive-ins, open-air cinemas and festivals. So the number of cinemas in 2025 is not directly comparable with earlier years. |
| Q2 | Based on a panel of 20,000 people (YouGov), so the numbers are estimates. Until 2018 only German citizens were counted, from 2019 everyone living in Germany. Children under 10 are only counted through adults. |
| Q3 | The interview part has 77 interviews (10 experts, 57 consumers in Germany, 10 in France). This is small and not representative. The definition of "arthouse cinema" changed in 2009/2010. |
| Q4, Q5 | Press texts, not data sources. The numbers should be taken from Q2 and Q3. |
| Q6, Q7 | Until 1989 only West Germany is counted, so the numbers jump in 1990. After the census in 2011 and 2022 the numbers were recalculated, so there are breaks in 2011 and 2022. The FFA uses different population numbers than Destatis. |
| Q8 | The number of cinemas in 2025 is not comparable with earlier years (see Q1). |

## Licences

**FFA (Q1, Q2, Q3, Q8):** The FFA reports have no open licence. Chaymae Loukili asked the FFA for permission for the group. On 27.10.2026, the FFA allowed the group to use their published numbers, combine them and publish them with the source. See [ffa_permission.md](ffa_permission.md).
The FFA PDFs and pictures from the reports are not uploaded to this repository.

How to cite:
- Source: Filmförderungsanstalt (FFA), Das Kinojahr 2025
- Source: Filmförderungsanstalt (FFA), Das Kinojahr, various years

**FFA press releases (Q4, Q5):** Only for quotes, with the source.

**Destatis (Q6, Q7):** [Data licence Germany – Attribution – Version 2.0](https://www.govdata.de/dl-de/by-2-0) (dl-de/by-2-0). This is an open licence. The data can be used and shared if the source is named.

How to cite: © Statistisches Bundesamt (Destatis), 2026
