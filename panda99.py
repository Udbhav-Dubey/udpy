import pandas as pd
d=['2025-05-21','2025-06-22']
res=pd.to_datetime(d)
print(res)
d=['2025-05-21','2025-06-22','invalid']
res=pd.to_datetime(d,format="%Y-%m-%d",errors="coerce")
print(res)
df = pd.DataFrame({'date': ['2025-06-21', '2025-06-22']})
df['date'] = pd.to_datetime(df['date'])
print(df)
d = ['21/06/2025', '22/06/2025']
res = pd.to_datetime(d, dayfirst=True)
print(res)
d = [0, 1, 2]
res = pd.to_datetime(d, unit='D', origin='2025-06-01')
print(res)
d = ['2025-06-21 12:00']
res = pd.to_datetime(d, utc=True)
print(res)
