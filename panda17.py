import pandas as pd
data=pd.read_csv("nba.csv",index_col="Name")
first=data.loc["Avery Bradley"]
second=data.loc["R.J. Hunter"]
print(first,"\n\n\n", second)
rows=data.loc[["Avery Bradley","R.J. Hunter"]]
print(type(rows))
print(rows)

