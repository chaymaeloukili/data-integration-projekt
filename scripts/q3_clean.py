# Q3 FFA tickets: cleaning script
# Input:  data/raw/ffa/ffa_tickets_total_arthouse_2001_2025.csv
# Output: data/processed/q3_ffa_tickets.csv

from pathlib import Path  # to work with file paths
import pandas as pd

# paths
ROOT = Path(__file__).resolve().parent.parent  # main folder of the project
DATA_FILE = ROOT / 'data/raw/ffa/ffa_tickets_total_arthouse_2001_2025.csv'  # raw data (input)
OUT_FILE = ROOT / 'data/processed/q3_ffa_tickets.csv'                      # clean data (output)

# loading the data
dataset = pd.read_csv(DATA_FILE)

# removing columns that are not needed for the analysis
dataset = dataset.drop(columns=['tickets_arthouse_million', 'arthouse_definition', 'source_id', 'source'])
print('Shape:', dataset.shape)  # expected: (25, 2)

# check for missing values
print('Missing values:')
print(dataset.isna().sum())  # 0 = nothing missing

# save the clean table
dataset.to_csv(OUT_FILE, index=False)
print('Saved to:', OUT_FILE)