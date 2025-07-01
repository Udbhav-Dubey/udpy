import pandas as pd
data=pd.read_csv("nba.csv")
data.dropna(inplace = True)
start,stop,step=0,-2,2
data["Name"]=data["Name"].str.slice(start,stop,step)
print(data.head(10))
