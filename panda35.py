import pandas as pd

df = pd.DataFrame({"A":[12, 4, 5, None, 1],
                "B":[5, 2, 54, 3, None],
                "C":[20, 16, 7, None, 8],
                "D":[14, None, 17, 2, 6]})

print(df)
ss1=df.mean(axis=0)
print(ss1)
ss2=df.mean(axis=1,skipna=True)
print(ss2)
#now applying on this only
sm1=ss1.mean()
sm2=ss2.mean(skipna=True)
print(sm1)
print(sm2)
