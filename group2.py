import pandas as pd

# Load the Excel file
file_path = "UG-IIa(2).xlsx"
df = pd.read_excel(file_path, engine="openpyxl")

# Clean the data
df_clean = df.dropna(how='all').dropna(axis=1, how='all')

# ----- Step 1: Detect columns that belong to 2S13 -----
class_code = "2S14"
matching_cols = []
for col in df_clean.columns:
    if df_clean[col].astype(str).head(10).str.contains(class_code).any():
        matching_cols.append(col)

# Identify time columns (adjust if needed)
day_col = df_clean.columns[0]      # Usually 'Day'
hour_col = df_clean.columns[3]     # Usually 'Hours'

# ----- Step 2: Ask user for day input -----
user_day = input("Enter a day (e.g., Monday): ").strip().lower()

# Normalize 'Day' column to lowercase string for matching
df_clean[day_col] = df_clean[day_col].astype(str).str.lower()

# ----- Step 3: Filter and show results -----
# Combine day, hour, and matching class columns
final_df = df_clean[[day_col, hour_col] + matching_cols]

# Filter for the specific day
day_df = final_df[final_df[day_col] == user_day]

# Remove rows where all class slots are NaN
day_df = day_df.dropna(subset=matching_cols, how='all')

# Show final filtered schedule
print("\nSchedule for", user_day.capitalize(), "for class", class_code)
print(day_df)

