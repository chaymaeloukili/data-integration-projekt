# Destatis data

Raw data from the Federal Statistical Office of Germany (Destatis), database GENESIS-Online.
The files are saved exactly as downloaded and are not changed.

| File | Source ID | Table | Content | Years |
|---|---|---|---|---|
| `12411-0001_de.csv` | Q6 | [12411-0001](https://genesis.destatis.de/datenbank/online/statistic/12411/table/12411-0001/search/s/Rm9ydHNjaHJlaWJ1bmclMjBkZXMlMjBCZXYlQzMlQjZsa2VydW5nc3N0YW5kZXM%3D) | Population of Germany | 1950–2025 |
| `12411-0003_de.csv` | Q7 | [12411-0003](https://genesis.destatis.de/datenbank/online/statistic/12411/table/12411-0003/search/s/Rm9ydHNjaHJlaWJ1bmclMjBkZXMlMjBCZXYlQzMlQjZsa2VydW5nc3N0YW5kZXM%3D) | Population of Germany by sex | 1970–2025 |

- Downloaded: 22.10.2026, by Chaymae Loukili
- Licence: [Data licence Germany – Attribution – Version 2.0](https://www.govdata.de/dl-de/by-2-0) (dl-de/by-2-0)
- How to cite: © Statistisches Bundesamt (Destatis), 2026

## How to read the files

- The files are in German. Separator: `;` (semicolon). Encoding: UTF-8.
- The first lines are a title, not data. The data starts with the first date.
- Each row is one year. The date is always 31 December (for example `31.12.2023`).
- `Anzahl` = number of people. `männlich` = male, `weiblich` = female, `Insgesamt` = total.
- `e` = final value (endgültig).
- The last lines are notes from Destatis.

## Important notes

- **Until 1989** the numbers are only for West Germany (Früheres Bundesgebiet). This is why the number jumps from 1989 to 1990.
- **From 2011 and from 2022** the numbers are based on a new census (Zensus 2011, Zensus 2022). This is why there are breaks in 2011 and 2022.
- The FFA uses different population numbers than Destatis. Example 2023: FFA 84,607,016, Destatis 83,456,045.
