import pandas as pd
t=pd.Timestamp("2000-10-15 11:22:33",tz='America/New_york')
print(t)
t=t.replace(hour=12,year=2006,second=21)
print(t)
