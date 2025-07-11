import pandas as pd
df=pd.read_csv("people_data.csv")
print(df)
df=pd.read_csv("people_data.csv",usecols=["First Name","Email"])
print(df)
df=pd.read_csv("people_data.csv",index_col="First Name")
print(df)
df=pd.read_csv("people_data.csv",na_values=["N/A","Unknown"])
print(df)

