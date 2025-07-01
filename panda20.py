import pandas as pd
data=pd.read_csv("nba.csv")
row1=data.iloc[3]
row2=data.loc[3]
row1==row2
print("row 1\n",row1)
print(row2)
row2=data.iloc[[4,5,6,7]]
row3=data.iloc[4:8]
print(row2)
print(row3)

