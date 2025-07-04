import pandas as pd
data=pd.read_csv("nba.csv")
col=data.head(5)
print(col)
clmn=list(col)
for i in clmn:
    print(col[i][2])
