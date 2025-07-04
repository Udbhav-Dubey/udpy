import pandas as pd
data=pd.read_csv("nba.csv")
print(data.head(5))
for i,j in data.iterrows():
    print(i,j)
    print()
