import pandas as pd
sr = pd.Series([11, 21, 8, 18, 65, 18, 32, 10, 5, 32, None])
print(sr)
index_=pd.date_range('2010-10-09 8:35',periods=11,freq='Y')
sr.index=index_
print(sr)
result = sr.apply(lambda x : True if x>30 else False)

print(result)
