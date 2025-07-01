import pandas as pd
data=pd.read_csv("nba.csv",index_col="Name")
selection=data.loc[["Avery Bradley", "R.J. Hunter"],["Team", "Number", "Position"]]
print(selection)
value=data.at["Avery Bradley","Team"]
print(value)
