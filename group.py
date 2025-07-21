import pandas as pd

file_path = "UG-IIa(2).xlsx"  # Make sure it's in your working directory or give full path
xls = pd.ExcelFile(file_path)

#print(xls.sheet_names)

# Load the correct sheet (adjust if needed)
df = pd.read_excel(xls, sheet_name=0)

# Drop rows with all NaN values
df_clean = df.dropna(how='all')

# Optional: Drop columns that are completely empty
df_clean = df_clean.dropna(axis=1, how='all')

# Display basic preview
#print(df_clean.head())

# Try to find rows that mention "2S14"
mask = df_clean.apply(lambda row: row.astype(str).str.contains("2S14").any(), axis=1)
df_2s14 = df_clean[mask]

# Display result
print(df_2s14)

# If there's a column named "Day" or "Hour", we can select them like this:
print(df_2s14[["Day", "Hour"]])

