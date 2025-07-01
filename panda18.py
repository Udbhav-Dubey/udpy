import pandas as pd
data=pd.read_csv("nba.csv",index_col="Team")
rows=data.loc["Utah Jazz"]
print(type(rows))
print(rows)
