import pandas as pd

file_path = "classtry.xlsx"
df = pd.read_excel(file_path, sheet_name="Sheet1")

columns_to_keep = ['DAY', 'HOURS', '2S1D']
df_group = df[columns_to_keep].copy()

df_group.dropna(how='all', inplace=True)

df_group['DAY'].ffill(inplace=True)
df_group['HOURS'].ffill(inplace=True)

df_group = df_group[df_group['2S1D'].notna()]

df_group.columns = ['Day', 'Time', 'Subject']

df_group.reset_index(drop=True, inplace=True)
print(df_group)

