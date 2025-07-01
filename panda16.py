import pandas as pd
data=pd.read_csv("nba.csv",index_col="Name")
print(data)
data.drop(["Team","Weight"],axis=1,inplace=True)
print(data)
