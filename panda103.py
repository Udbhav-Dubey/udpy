import pandas as pd
data=pd.read_csv("nba.csv")
data["Age"]=data["Age"].replace(25.0,"Twenty-five")
filter=data["Age"]=="Twenty-five"
print(data.where(filter).dropna().head(n=20))

