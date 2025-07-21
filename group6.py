import pandas as pd
file_path = "classtry.xlsx"
df = pd.read_excel(file_path, sheet_name="Sheet1")
print(df[23:46])
