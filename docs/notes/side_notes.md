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
- `data/raw/ffa/ffa_german_market_share_2001_2025.csv` will only be cleaned if we keep Letterboxd (licence and data still open). To be decided at the check-up on 19.11.2026 or the meeting on 24.11.2026.

---
### 24.11.2026, Hafssa

**Q6 scripts moved**

What I changed:
- `scripts/q6_destatis_population/02_clean.py` is now `scripts/q6_clean.py`, directly in `scripts/` like `q3_clean.py` (run from the main folder: `python scripts/q6_clean.py`). The path to the main folder in the script was adjusted (`parents[1]`).
- Removed `scripts/q6_destatis_population/01_explore.py`.

Why:
- The explore and clean steps are in the notebooks, so one clean script per source is enough.
- All clean scripts should be directly in `scripts/` with the name `q<number>_clean.py`.
- The output `data/processed/q6_destatis_population.csv` did not change (25 rows, 2001–2025).
