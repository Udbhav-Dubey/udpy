import pandas as pd
data=pd.read_csv("nba.csv")
print(data)
data.sort_values("Salary",axis=0,ascending=True,inplace=True,na_position='first')
print(data)
