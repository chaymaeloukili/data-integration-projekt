import pandas as pd

# ==================================================
# DATA CLEANING
# Dataset: FFA Cinema Key Figures (2021–2025)
# ==================================================

# Load the original dataset
df = pd.read_csv("ffa_kinojahr_key_figures_2021_2025.csv")

# Create a working copy
df_clean = df.copy()

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
numeric_columns = df_clean.select_dtypes(include="number").columns.drop("year")

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

# Compare the original and cleaned DataFrames
data_unchanged = df.equals(df_clean)

print("\nOriginal dataset shape:", df.shape)
print("Cleaned dataset shape:", df_clean.shape)
print("Data unchanged:", data_unchanged)

if data_unchanged:
    print("No modifications were necessary.")
    print("The dataset passed the performed cleaning checks.")

print("\n--- DATA CLEANING COMPLETED ---")
