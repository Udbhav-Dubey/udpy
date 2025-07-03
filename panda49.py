import pandas as pd
sr=pd.Series(['J&k','Pb','Hr','Ka','Rj','Up'])
didx=pd.date_range('2014-08-01 10:00',periods=6,freq='W',tz='Europe/Berlin')
sr.index=didx
print(sr)
result=sr.truncate(before = '2014-08-17 10:00:00+02:00')
print(result)
