"""Clean Q2 (FFA Kinobesucher*innen 2025). Decisions: notebooks/q2_ffa_visitors/q2_explore.ipynb"""
from pathlib import Path

import pandas as pd

PROJECT = Path(__file__).resolve().parent.parent.parent
RAW = PROJECT / "data" / "raw" / "ffa"
PROCESSED = PROJECT / "data" / "processed"
PROCESSED.mkdir(parents=True, exist_ok=True)
METADATA = ["source_id", "source"]

# File 1: spending
spending = pd.read_csv(RAW / "ffa_spending_cinema_homevideo_2003_2025.csv").drop(columns=METADATA)
assert spending["year"].is_unique and len(spending) == 23

# File 2: age and gender
age_gender = (
    pd.read_csv(RAW / "ffa_visitors_age_gender_2021_2025.csv")
    .drop(columns=METADATA)
    .rename(columns={"tickets_base_million": "tickets_panel_million"})
)
age_columns = ["age_10_19_percent", "age_20_29_percent", "age_30_39_percent",
               "age_40_49_percent", "age_50_59_percent", "age_60_plus_percent"]
assert age_gender["year"].is_unique and len(age_gender) == 5
assert (age_gender["male_percent"] + age_gender["female_percent"] == 100).all()
assert age_gender[age_columns].sum(axis=1).between(99, 101).all()

# File 3: reach
reach = pd.read_csv(RAW / "ffa_visitors_reach_2015_2025.csv").drop(columns=METADATA)
reach["reach_survey_population"] = "all_residents"
reach.loc[reach["year"] <= 2018, "reach_survey_population"] = "german_citizens"
assert reach["year"].is_unique and len(reach) == 11

# Merge by year (file 4 not merged: rows are groups, not years)
q2 = (
    spending
    .merge(reach, on="year", how="left", validate="one_to_one")
    .merge(age_gender, on="year", how="left", validate="one_to_one")
    .sort_values("year")
    .reset_index(drop=True)
)
assert len(q2) == 23 and len(q2.columns) == 24

output = PROCESSED / "q2_ffa_visitors_clean.csv"
q2.to_csv(output, index=False)
print(f"Saved {len(q2)} rows and {len(q2.columns)} columns to {output}")