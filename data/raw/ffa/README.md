# FFA data

Data from the FFA (Filmförderungsanstalt, German Federal Film Board).
The FFA allowed the use and publication of their numbers with the source, see [ffa_permission.md](../../../docs/sources/ffa_permission.md).
The original FFA files (PDFs, PowerPoint) are not uploaded.

## ffa_cinemas_arthouse_2016_2025.csv

Source ID: Q8

- Content: Number of cinemas and tickets per year, in all cinemas and in arthouse cinemas (Programmkinos)
- Years: 2016–2025
- Origin: PowerPoint file sent by the FFA on 27.10.2026. The numbers were taken from the tables inside the charts and saved as CSV by Chaymae Loukili. The same numbers are also in "Das Kinojahr 2025".
- How to cite: Source: Filmförderungsanstalt (FFA), Das Kinojahr 2025
- Separator: `,` (comma). Decimal point: `.`

| Column | Meaning |
|---|---|
| `year` | Year |
| `cinemas_total` | Number of cinema venues in Germany |
| `cinemas_with_arthouse` | Number of venues with arthouse cinema (Programmkino), as counted by the FFA |
| `tickets_total_million` | Tickets sold in all cinemas, in million |
| `tickets_arthouse_million` | Tickets sold in arthouse cinemas, in million |

## Important notes

- From 2025, the FFA counts cinemas without drive-in cinemas, open-air cinemas and festivals. So `cinemas_total` for 2025 is not directly comparable with earlier years.
- 2020 and 2021: Cinemas were closed for months because of COVID-19.
