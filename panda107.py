import pandas as pd
data=pd.read_csv("nba.csv")
filter=data["College"]=="Texas"
print(data.where(filter).dropna())
