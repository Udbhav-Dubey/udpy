import pandas as pd
data=pd.read_csv("nba.csv")
print("DataSet")
print(data.head(5))
first=data["Age"]
print(first.head())
#selection=data.loc[["Avery Bradley", "R.J. Hunter"],["Team", "Number", "Position"]]
#print(selection)
value=data.at["Avery Bradley","Team"]
print(value)
