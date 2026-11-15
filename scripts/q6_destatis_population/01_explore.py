# Explore Destatis table 12411-0001. Run: python scripts/q6_destatis_population/01_explore.py
from pathlib import Path

import matplotlib.pyplot as plt
import pandas as pd

ROOT = Path(__file__).resolve().parents[2]
RAW = ROOT / "data" / "raw" / "destatis" / "12411-0001_de.csv"

with open(RAW, encoding="utf-8-sig") as f:
    lines = f.read().splitlines()

print("Number of lines:", len(lines))
print("--- Beginning ---")
for l in lines[:10]:
    print(repr(l))
print("--- End ---")
for l in lines[-10:]:
    print(repr(l))

first_data = next(i for i, l in enumerate(lines) if l[:2].isdigit())
last_data = max(i for i, l in enumerate(lines) if l[:2].isdigit())
print("first data row:", first_data, "| last data row:", last_data)

df = pd.read_csv(RAW, sep=";", encoding="utf-8-sig", header=None,
                 skiprows=first_data, nrows=last_data - first_data + 1,
                 names=["date_raw", "population_raw", "value_status"])
print(df.head())

print(df.shape)
df.info()

print(df.isna().sum())
print(df["value_status"].value_counts())
print(df["population_raw"].astype(str).str.contains(r"[^0-9]").sum(), "non-digit values")

df["year"] = pd.to_datetime(df["date_raw"], format="%d.%m.%Y").dt.year
print("Years:", df["year"].min(), "to", df["year"].max())
print("Years unique:", df["year"].is_unique)
missing = sorted(set(range(df["year"].min(), df["year"].max() + 1)) - set(df["year"]))
print("Missing years:", missing)

sub = df[df["year"].between(2001, 2025)]
print(sub["population_raw"].describe())

ax = df.set_index("year")["population_raw"].plot(figsize=(9, 4), marker="o", markersize=3)
ax.set_title("Population Germany, reference date 31.12. (raw data)")
ax.set_ylabel("Number of persons")
for y in (1990, 2011, 2022):
    ax.axvline(y, color="grey", linestyle=":")
plt.show()

change = df.set_index("year")["population_raw"].diff().loc[2001:2025]
print(change.sort_values().head(3))
print(change.sort_values().tail(3))