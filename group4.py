import pandas as pd
file_path = "classtry.xlsx"
df = pd.read_excel(file_path, engine="openpyxl")
print(df.head())

mask = df.apply(lambda row: row.astype(str).str.contains("2S1D").any(), axis=1)
df_2s14 = df[mask]

print(df_2s14.head(n=23))
