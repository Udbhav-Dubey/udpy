import pandas as pd
df=pd.read_csv("pandacsv.csv")
print(df)
ser=df['Name']
print(ser)
print("now using loc we do first 2 : ")
print(ser.loc[0:2])
print(df.iloc[0:2,0])
