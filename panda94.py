import pandas as pd
url='http://bit.ly/uforeports'
df=pd.read_csv(url)
print(df.head())
df["Time"]=pd.to_datetime(df.Time)
print(df.head())
print(df.Time.dt.hour.head()) 
print(df.Time.dt.dayofyear.head())
