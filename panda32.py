import pandas as pd
df=pd.DataFrame({'A':[1,2,3],'B':[4,5,6],'C':[7,8,9]})
print(df)
df['add']=df['A']+df['B']+df['C']
print(df)
import numpy as np
df['np_add_1']=np.sum(df[['A','B','C']].values,axis=1)
print(df)
df['np_add_0']=np.sum(df[['A','B','C']].values,axis=0)
print(df)
res=[]
for row in df.itertuples(index=False):
    res.append(row.A+row.B+row.C)
df['res_add']=res
print(df)
df['list_add'] = [a + b + c for a, b, c in zip(df['A'], df['B'], df['C'])]
print(df)
