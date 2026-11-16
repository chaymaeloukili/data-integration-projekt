### 16.11.2026, Chaymae

**Q3 cleaning done** (deadline was 20.11.2026)

What I added or changed:
- `notebooks/q3_ffa_tickets/01_explore.ipynb`: explored the raw data, wrote first observations and questions for the analysis
- `notebooks/q3_ffa_tickets/02_clean.ipynb`: cleaning steps with explanations
- `scripts/q3_clean.py`: same cleaning steps as a script (run from the main folder: `python scripts/q3_clean.py`)
- `data/processed/q3_ffa_tickets.csv`: new clean table with `year` and `tickets_total_million`, 25 rows (2001–2025)
- `notebooks/q3_ffa_tickets/README.md`: updated (steps, status, known issues)
- `AI_USAGE.md`: added my entries for 16.11.2026

Why:
- Only `year` and `tickets_total_million` are needed for our research questions. Four columns were removed (see the summary in `02_clean.ipynb`).
- The raw data in `data/raw/ffa/` was **not** changed.

Later:
- `data/raw/ffa/ffa_german_market_share_2001_2025.csv` will be cleaned later, so it can be combined with Letterboxd.
