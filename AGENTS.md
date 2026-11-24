# AGENTS.md

Instructions for AI coding agents (GitHub Copilot, Claude, ChatGPT and others) in this repository.

## Project

Group project for DIS 3.3 Data Integration (TH Köln, winter semester 2026/27): **Cinema Visits in Germany (2001–2025)**.
Main question: How will movie attendance in Germany change by 2026? The sub-questions, the folder structure and the plan are in `README.md`.

## Setup and commands

We have no `requirements.txt` yet. Until then:

- Python 3, with the packages `pandas`, `matplotlib` and `jupyter`.
- Create and activate a virtual environment:
  - macOS: `python3 -m venv .venv` and `source .venv/bin/activate`
  - Windows: `python -m venv .venv` and `.venv\Scripts\activate.bat`
- Install the packages: `python -m pip install pandas matplotlib jupyter`
- Run each script from the main folder of the repository, e.g. `python scripts/q1_cinema_key_figures/q1_cleaning.py`.
- Open notebooks in VS Code or with `jupyter notebook`, and run them from top to bottom.
- Tests: none yet. When we add them, they run with `python -m pytest`.

## Documentation

- After every team meeting, we write a protocol in `docs/meetings/` (see `docs/meetings/README.md`).

## Data

*To be added by Aqsa: sources with link and licence, units, and known data problems.*

## Rules for AI Agents

### 1. Raw Data Protection
- Never modify, delete or overwrite files in `data/raw/`.
- Treat all original datasets as read-only.
- Do not commit raw datasets to Git.
- Save cleaned and transformed data separately in `data/processed/`.

### 2. Data Quality
- Do not silently remove or fill missing values.
- Report missing values, duplicates and unexpected data types.
- Check the number of rows before and after filtering or merging.
- Preserve the original units and document all conversions.
- Do not change column names without explaining the changes.
- Check that datasets use compatible years, country names and units before merging.
- Do not treat missing values as zero unless this is explicitly justified.

### 3. Privacy and Data Sources
- Never include personal or sensitive information in AI prompts.
- Do not invent data sources, URLs or licence information.
- Respect the licences and usage conditions of all datasets.
- Ask before using data from a source with unclear permissions.
- Do not download or scrape data from IMDb, Letterboxd or similar platforms without checking their terms of use and permissions.

### 4. Code and Testing
- Do not modify existing tests without permission.
- Run tests after code changes and report the results.
- Do not install additional Python packages without approval.
- Make only the requested changes and avoid unnecessary modifications.
- Explain planned changes before implementing them.

### 5. AI Usage and Human Review
- Document every use of AI in `AI_USAGE.md`.
- Record the AI tool, model, purpose and important prompts.
- Document which suggestions were accepted, modified or rejected.
- Do not commit or push changes without human approval.
- All AI-generated code and results must be reviewed by a team member.