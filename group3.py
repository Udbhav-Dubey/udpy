import pandas as pd

# Load Excel
file_path = "UG-IIa(2).xlsx"
df = pd.read_excel(file_path, engine="openpyxl")

# Clean the data
df_clean = df.dropna(how='all').dropna(axis=1, how='all')

# DEBUG: Show first 10 rows of the first few columns
print("\n==== PREVIEW ====")
print(df_clean.iloc[:10, :5])  # See first few rows and columns

# Define columns manually (based on your message)
day_col = df_clean.columns[0]    # Unnamed: 0
hour_col = df_clean.columns[3]   # Unnamed: 3
class_col = df_clean.columns[22] # Unnamed: 22 (2S14 column)

# DEBUG: Show unique values in day_col to verify format
print("\n==== UNIQUE DAYS ====")
print(df_clean[day_col].dropna().unique())

# Filter for Monday (case-insensitive match)
monday_df = df_clean[
    df_clean[day_col].astype(str).str.lower().str.strip() == "monday"
]

# Drop rows where the class column is empty
monday_df = monday_df.dropna(subset=[class_col], how='all')

# Final output
print("\n==== MONDAY SCHEDULE FOR 2S14 ====")
print(monday_df[[day_col, hour_col, class_col]])

