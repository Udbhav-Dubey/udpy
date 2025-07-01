import pandas as pd
data=pd.read_csv("nba.csv",index_col="Name")
print(data['Age']>25)
