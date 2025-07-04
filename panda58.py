import pandas as pd
data=pd.read_csv("nba.csv")
for i in data.itertuples():
    print(i)
