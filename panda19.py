import pandas as pd
data=pd.read_csv("nba.csv",index_col="Name")
rows=data.loc["Avery Bradley": "Isaiah Thomas"]
print(type(rows))
print(rows)
