import pandas as pd
data=pd.read_csv("nba.csv")
data.dropna(inplace=True)
data["Name"]=data["Name"].str.join("-")
print(data)
data["Team"]=data["Team"].str.split("t")
print(data)
data["Team"]=data["Team"].str.join("_")
print(data)
