"""Explore Q2 (FFA Kinobesucher*innen 2025). Findings: notebooks/q2_ffa_visitors/q2_explore.ipynb"""
from pathlib import Path

import pandas as pd

PROJECT = Path(__file__).resolve().parent.parent.parent
RAW = PROJECT / "data" / "raw" / "ffa"
pd.set_option("display.max_columns", None)
pd.set_option("display.width", 200)

files = [
    "ffa_spending_cinema_homevideo_2003_2025.csv",
    "ffa_visitors_age_gender_2021_2025.csv",
    "ffa_visitors_reach_2015_2025.csv",
    "ffa_cinema_svod_subscribers_2025.csv",
]
dfs = {f: pd.read_csv(RAW / f) for f in files}

# Overview of all files
for name, df in dfs.items():
    print(f"\n=== {name} ===")
    print("Shape:", df.shape)
    df.info()
    print(df.head())
    missing = df.isna().sum()
    print("Missing values:\n", missing[missing > 0])

# File 1: total vs. sum of categories, first year with SVOD
spending = dfs["ffa_spending_cinema_homevideo_2003_2025.csv"]
parts = ["cinema_million_eur", "dvd_bluray_vhs_million_eur",
         "est_tvod_million_eur", "svod_million_eur"]
difference = spending["total_million_eur"] - spending[parts].sum(axis=1)
print("\nFile 1: total minus sum (min, max):", difference.min(), difference.max())
print("File 1: first year with SVOD:", spending.loc[spending["svod_million_eur"].notna(), "year"].min())

# File 2: gender and age sums
age_gender = dfs["ffa_visitors_age_gender_2021_2025.csv"]
age_columns = ["age_10_19_percent", "age_20_29_percent", "age_30_39_percent",
               "age_40_49_percent", "age_50_59_percent", "age_60_plus_percent"]
print("\nFile 2: sums per year")
print(pd.DataFrame({
    "year": age_gender["year"],
    "gender_sum": age_gender["male_percent"] + age_gender["female_percent"],
    "age_sum": age_gender[age_columns].sum(axis=1),
}))

# File 3: implied population base and tickets
reach = dfs["ffa_visitors_reach_2015_2025.csv"]
print("\nFile 3: implied population and tickets")
print(pd.DataFrame({
    "year": reach["year"],
    "implied_population_million": reach["cinema_visitors_million"] / reach["cinema_reach_percent"] * 100,
    "implied_tickets_million": reach["cinema_visitors_million"] * reach["visits_per_person"],
}).round(1))