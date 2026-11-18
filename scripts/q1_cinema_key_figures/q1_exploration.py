
import pandas as pd
from pathlib import Path

# ==================================================
# DATA EXPLORATION
# Dataset: FFA Cinema Key Figures (2021–2025)
# Source: Filmförderungsanstalt (FFA)
# ==================================================

# Define the repository root directory
project_root = Path(__file__).resolve().parents[2]

# Define the input dataset path
input_file = (
    project_root
    / "data"
    / "processed"
    / "q1_ffa_kinojahr_key_figures_2021_2025.csv"
)

# Load the dataset
df = pd.read_csv(input_file)


# --------------------------------------------------
# STEP 1: DATA STRUCTURE
# --------------------------------------------------

print("\n--- DATA STRUCTURE ---")

print("\nFirst five rows:")
print(df.head().to_string(index=False))

print("\nDataset shape (rows, columns):")
print(df.shape)

print("\nColumn names:")
print(df.columns.tolist())

print("\nData types and non-null values:")
df.info()


# --------------------------------------------------
# STEP 2: MISSING VALUES
# --------------------------------------------------

print("\n--- MISSING VALUES ---")

print("\nMissing values per column:")
print(df.isnull().sum())

print("\nTotal missing values:")
print(df.isnull().sum().sum())


# --------------------------------------------------
# STEP 3: DUPLICATE CHECK
# --------------------------------------------------

print("\n--- DUPLICATE CHECK ---")

print("\nFully duplicated rows:")
print(df.duplicated().sum())

print("\nDuplicated years:")
print(df["year"].duplicated().sum())


# --------------------------------------------------
# STEP 4: STATISTICAL OVERVIEW
# --------------------------------------------------

print("\n--- STATISTICAL OVERVIEW ---")

print(df.describe().to_string())


# --------------------------------------------------
# STEP 5: PLAUSIBILITY CHECK
# --------------------------------------------------

print("\n--- PLAUSIBILITY CHECK ---")

print("\nNegative ticket counts:")
print((df["tickets"] < 0).sum())

print("\nNegative revenue values:")
print((df["revenue_eur"] < 0).sum())

print("\nInvalid average ticket prices:")
print((df["avg_ticket_price_eur"] <= 0).sum())

print("\nInvalid German film market shares:")
print((
    (df["market_share_german_films_percent"] < 0) |
    (df["market_share_german_films_percent"] > 100)
).sum())


# --------------------------------------------------
# STEP 6: CONSISTENCY CHECK
# --------------------------------------------------

print("\n--- CONSISTENCY CHECK ---")

# Create a separate DataFrame for comparison
comparison = df[[
    "year",
    "tickets",
    "avg_ticket_price_eur",
    "revenue_eur"
]].copy()

# Calculate revenue using ticket counts and average prices
comparison["calculated_revenue"] = (
    comparison["tickets"] *
    comparison["avg_ticket_price_eur"]
)

# Calculate the difference between reported and calculated revenue
comparison["revenue_difference"] = (
    comparison["revenue_eur"] -
    comparison["calculated_revenue"]
)

print(comparison.to_string(index=False))


# --------------------------------------------------
# STEP 7: TEXT COLUMN CHECK
# --------------------------------------------------

print("\n--- TEXT COLUMN CHECK ---")

print("\nUnique source IDs:")
print(df["source_id"].unique())

print("\nUnique sources:")
print(df["source"].unique())


# --------------------------------------------------
# STEP 8: YEAR RANGE CHECK
# --------------------------------------------------

print("\n--- YEAR RANGE CHECK ---")

print("\nAvailable years:")
print(sorted(df["year"].tolist()))

print("\nMinimum year:")
print(df["year"].min())

print("\nMaximum year:")
print(df["year"].max())

# Compare available years with the expected time range
expected_years = set(range(2021, 2026))
available_years = set(df["year"])

missing_years = expected_years - available_years

print("\nMissing years:")
print(sorted(missing_years))


# --------------------------------------------------
# EXPLORATION COMPLETED
# --------------------------------------------------

print("\n--- DATA EXPLORATION COMPLETED ---")
