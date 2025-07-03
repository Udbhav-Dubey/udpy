import pandas as pd
df=pd.DataFrame({
                'a':[12,4,5,None,1],
                'b':[7,2,54,3,None],
                'c':[20,16,11,3,8],
                'd':[14,3,None,2,6]})
index_=['Row 1','Row 2','Row 3','Row 4','Row 5']
df.index=index_
print(df)
result=df.truncate(before='Row 3',after='Row 4')

print(result)
