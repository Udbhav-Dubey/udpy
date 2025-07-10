import pandas as pd
ts = pd.Timestamp('2019-10-10 07:15:11')
do = pd.tseries.offsets.DateOffset(n=2)
print(ts)
print(do)
new_timestamp = ts + do
print(new_timestamp)
do=pd.tseries.offsets.DateOffset(days=10,hours=2)
print(do)
new_ts=ts+do
print(new_ts)
date = pd.Timestamp('2023-12-22')
offset = pd.DateOffset(months=-2)
new_date = date + offset
print(new_date)  

dates = pd.date_range('2023-12-20', periods=5, freq='D')
offset = pd.DateOffset(days=3)
new_dates = dates + offset
print(new_dates)
