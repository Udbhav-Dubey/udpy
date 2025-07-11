import pandas as pd
excel=pd.ExcelFile("kite.xlsx")
print(excel.sheet_names)
df=excel.parse('Sheet2')
print(df.dropna())
require_cols = [0, 3] 
required_df = pd.read_excel('kite.xlsx', usecols = require_cols) 
print(required_df)
