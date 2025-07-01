import pandas as pd
data={'Name': ['ud','bh','av'],
      'Age' : [11,13,15],
      'class': [6,8,10],
      'subject':['math','science','sst']}
df=pd.DataFrame(data)
print(df)
df1=df[['Name','subject']]
print(df1)
df2=df[df.columns[1:4]]
print(df2)
df3=df.loc[1:2,['Name','Age']]
print(df3)
df4=df.loc[1:2]
print(df4)
df5=df.iloc[:,1:2]
print(df5)
df6=df.iloc[0:2,1:3]
print(df6)
df7=df.ix[:,0:2]
print(df7)
