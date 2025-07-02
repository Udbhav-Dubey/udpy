import pandas as pd
s=pd.Series([1,2,3,4])
result=s.apply(lambda x : x**2)
print(result)
df=pd.DataFrame({
    'A':[1,2,3],
    'B':[10,20,30]
})
print(df)
result=df.apply(sum,axis=0)
print(result)
result=df.apply(sum,axis=1)
print(result)

