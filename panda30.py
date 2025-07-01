import pandas as pd

df1 = pd.DataFrame({"a": [1, 2, 3, 4, 5, 6, 7], 
                    "b": [2, 3, 4, 2, 3, 4, 5], 
                    "c": [3, 4, 5, 2, 3, 4, 5], 
                    "d": [4, 5, 6, 2, 3, 4, 5], 
                    "e": [5, 6, 7, 2, 3, 4, 5]})

print(df1)
df2=df1.reindex(columns=['c','b'])
print(df2)
#method 2
df3=df1.loc[:,"b":"d":2]
print(df3)
#method 3
df4=df1.iloc[:,1:3:1]
print(df4)
