import pandas as pd
data=pd.read_csv("nba.csv")
print(data.head())
data.sort_values("Name",axis=0,ascending=True,inplace=True,na_position='last')
print(data)

