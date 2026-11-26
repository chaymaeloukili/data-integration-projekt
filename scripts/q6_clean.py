# Clean Destatis table 12411-0001 -> data/processed/q6_destatis_population.csv. Run: python scripts/q6_clean.py
from pathlib import Path

import pandas as pd

ROOT = Path(__file__).resolve().parents[1]
RAW = ROOT / "data" / "raw" / "destatis" / "12411-0001_de.csv"
OUT = ROOT / "data" / "processed" / "q6_destatis_population.csv"

with open(RAW, encoding="utf-8-sig") as f:
    lines = f.read().splitlines()

first_data = next(i for i, l in enumerate(lines) if l[:2].isdigit())
last_data = max(i for i, l in enumerate(lines) if l[:2].isdigit())

df = pd.read_csv(RAW, sep=";", encoding="utf-8-sig", header=None,
                 skiprows=first_data, nrows=last_data - first_data + 1,
                 names=["date_raw", "population_raw", "value_status"])

df["year"] = pd.to_datetime(df["date_raw"], format="%d.%m.%Y").dt.year
clean = (df[df["year"].between(2001, 2025)]
         .rename(columns={"population_raw": "population"})
         [["year", "population"]]
         .reset_index(drop=True))
print(clean.shape)

assert len(clean) == 25
assert clean["year"].is_unique
assert clean.isna().sum().sum() == 0
assert clean.loc[clean["year"] == 2025, "population"].item() == 83467117
print("All checks passed")

clean.to_csv(OUT, index=False)
print("Saved to:", OUT)
print(pd.read_csv(OUT).head())