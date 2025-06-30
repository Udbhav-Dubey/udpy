import pandas as pd
data=pd.read_csv("nba.csv")
print("Nba Dataset : ")
print(data.head())
print("summary table genrated by .describe() Method: ")
print(data.describe())
percentiles=[.20,.40,.60,.80]
include =["object","float","int"]
desc=data.describe(percentiles=percentiles,include=include)
print(desc)
