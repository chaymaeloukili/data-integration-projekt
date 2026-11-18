import pandas as pd
from pathlib import Path

# ==================================================
# DATA CLEANING
# Dataset: FFA Cinema Key Figures (2021–2025)
# Source: Filmförderungsanstalt (FFA)
# ==================================================

# Define the repository root directory
project_root = Path(__file__).resolve().parents[2]

# Define input and output paths
input_file = (
    project_root
    / "data"
    / "processed"
    / "q1_ffa_kinojahr_key_figures_2021_2025.csv"
)

output_file = (
    project_root
    / "data"
    / "processed"
    / "q1_ffa_kinojahr_key_figures_2021_2025_clean.csv"
)

# Load the original dataset
df = pd.read_csv(input_file)

# Create a working copy
df_clean = df.copy()


# --------------------------------------------------
# STEP 1: CREATE WORKING COPY
# --------------------------------------------------

print("\n--- DATA CLEANING ---")

print("\nOriginal dataset shape:")
print(df.shape)

print("\nWorking copy shape:")
print(df_clean.shape)

print("\nAre both datasets identical?")
print(df.equals(df_clean))


# --------------------------------------------------
# STEP 2: VALIDATE MISSING VALUES AND DUPLICATES
# --------------------------------------------------

print("\n--- MISSING VALUES AND DUPLICATES ---")

missing_values = df_clean.isnull().sum().sum()
duplicate_rows = df_clean.duplicated().sum()
duplicate_years = df_clean["year"].duplicated().sum()

print("\nTotal missing values:", missing_values)
print("Duplicate rows:", duplicate_rows)
print("Duplicate years:", duplicate_years)

if missing_values == 0:
    print("No missing values found. No cleaning required.")

if duplicate_rows == 0 and duplicate_years == 0:
    print("No duplicates found. No cleaning required.")


# --------------------------------------------------
# STEP 3: DATA TYPE VALIDATION
# --------------------------------------------------

print("\n--- DATA TYPE VALIDATION ---")

expected_types = {
    "year": "int64",
    "population_ffa": "int64",
    "tickets": "int64",
    "revenue_eur": "int64",
    "avg_ticket_price_eur": "float64",
    "cinema_companies": "int64",
    "locations": "int64",
    "venues": "int64",
    "screens": "int64",
    "seats": "int64",
    "tickets_german_films_million": "float64",
    "market_share_german_films_percent": "float64",
    "tickets_3d_million": "float64",
    "source_id": "object",
    "source": "object"
}

for column, expected_type in expected_types.items():
    actual_type = str(df_clean[column].dtype)

    if actual_type == expected_type:
        print(f"{column}: OK ({actual_type})")
    else:
        print(
            f"{column}: Type mismatch! "
            f"Expected {expected_type}, found {actual_type}"
        )


# --------------------------------------------------
# STEP 4: FINAL DATA QUALITY VALIDATION
# --------------------------------------------------

print("\n--- FINAL DATA QUALITY VALIDATION ---")

# Select all numeric columns except the year
numeric_columns = (
    df_clean.select_dtypes(include="number")
    .columns.drop("year")
)

# Check for negative values
negative_values = (df_clean[numeric_columns] < 0).sum()

print("\nNegative values per numeric column:")
print(negative_values)

print("\nTotal negative values:")
print(negative_values.sum())

# Check market share range
invalid_market_share = (
    (df_clean["market_share_german_films_percent"] < 0) |
    (df_clean["market_share_german_films_percent"] > 100)
).sum()

print("\nInvalid market share values:")
print(invalid_market_share)


# --------------------------------------------------
# STEP 5: FINAL VERIFICATION
# --------------------------------------------------

print("\n--- FINAL VERIFICATION ---")

# Compare original and working DataFrames
data_unchanged = df.equals(df_clean)

print("\nOriginal dataset shape:", df.shape)
print("Cleaned dataset shape:", df_clean.shape)
print("Data unchanged:", data_unchanged)

if data_unchanged:
    print("No modifications were necessary.")
    print("The dataset passed the performed cleaning checks.")


# --------------------------------------------------
# STEP 6: FEATURE SELECTION
# --------------------------------------------------

print("\n--- FEATURE SELECTION ---")

# Define columns not relevant to the research question
columns_to_remove = [
    "cinema_companies",
    "locations",
    "venues",
    "seats",
    "tickets_german_films_million",
    "market_share_german_films_percent",
    "tickets_3d_million"
]

# Remove irrelevant columns from the working copy
df_clean = df_clean.drop(columns=columns_to_remove)

print("\nRemaining columns:")
print(df_clean.columns.tolist())

print("\nOriginal dataset shape:")
print(df.shape)

print("\nPrepared dataset shape:")
print(df_clean.shape)


# --------------------------------------------------
# STEP 7: EXPORT PROCESSED DATASET
# --------------------------------------------------

print("\n--- EXPORT PROCESSED DATASET ---")

# Save the prepared dataset as a new CSV file
df_clean.to_csv(output_file, index=False)

print(f"Processed dataset saved as: {output_file}")
print(f"Final dataset shape: {df_clean.shape}")


# --------------------------------------------------
# STEP 8: VERIFY EXPORTED DATASET
# --------------------------------------------------

print("\n--- VERIFY EXPORTED DATASET ---")

# Read the exported CSV file
df_exported = pd.read_csv(output_file)

# Verify structure and content
print("\nExported dataset shape:")
print(df_exported.shape)

print("\nExported data matches prepared data:")
print(df_exported.equals(df_clean))

print("\nExported dataset:")
print(df_exported.to_string(index=False))


# --------------------------------------------------
# CLEANING COMPLETED
# --------------------------------------------------

print("\n--- DATA CLEANING COMPLETED ---")
