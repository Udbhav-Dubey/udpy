import pandas as pd
dict={'Name':["ud","bh","av"],
      'class':[1,2,3],
      'score':[90,80,70]}
df=pd.DataFrame(dict,index=[True,False,True])
print(df)
print(df.loc[True])
print(df.iloc[2])
