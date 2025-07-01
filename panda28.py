import pandas as pd
data=pd.read_csv("nba.csv")
data.dropna(inplace=True)
print(data)
start,stop,step=0,-2,1
data["Salary"]=data["Salary"].astype(str)
data["Salary (int)"]=data["Salary"].str.slice(start,stop,step)
print(data.head(10))
