import pandas as pd
data=pd.read_csv("nba.csv")
#new=data["Team"].copy()
data["Name"]=data["Name"].str.cat(data["Team"],sep=", ")
print(data)
na_string="No college"
data["College"]=data["College"].str.cat(data["Team"],sep=", ",na_rep=na_string)
print(data)
