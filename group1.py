import pandas as pd

# Load the Excel file
file_path = "UG-IIa(2).xlsx"  # Make sure file is in the same folder or give full path
df = pd.read_excel(file_path, engine="openpyxl")

# Drop fully empty rows and columns
df_clean = df.dropna(how='all').dropna(axis=1, how='all')

# Search for column names or cells that contain "2S13"
class_code = "2S14"

# We'll look in the first 10 rows to detect which columns have "2S13"
matching_cols = []
for col in df_clean.columns:
    # Convert cells to string and check for class code
    if df_clean[col].astype(str).head(10).str.contains(class_code).any():
        matching_cols.append(col)

print("Columns that include class 2S13:", matching_cols)

# Now, extract the time-related info. We'll assume day/hour is in the first few columns
# Let’s say columns 0 and 3 are "Day" and "Hours" based on your file
time_cols = [df_clean.columns[0], df_clean.columns[3]]

# Combine them with matching class columns
final_df = df_clean[time_cols + matching_cols]

# Optional: remove rows where the 2S13 column is NaN (i.e., class doesn't have slot then)
final_df = final_df.dropna(subset=matching_cols, how='all')

# Show final cleaned class schedule for 2S13
print(final_df)
