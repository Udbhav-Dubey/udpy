import pandas as pd
timestamp=pd.Timestamp("2006-01-04 15:20:31",tz='Asia/Kolkata')
print(timestamp)
utc_ts = timestamp.tz_convert('UTC')
print(utc_ts)
original_time=utc_ts.tz_convert('Asia/Kolkata')
print(original_time)
datetime_index = pd.DatetimeIndex(['2023-10-04',
                                   '2023-10-11', 
                                   '2023-10-18'],
                                  tz='America/New_York')
print(datetime_index)
utc_tss=datetime_index.tz_convert('UTC')
print(utc_tss)
original=utc_tss.tz_convert('America/New_York')
print(original)

raw=pd.Timestamp("20:00:00",tz='America/New_York')
print(raw)
utc_raw=raw.tz_convert('Asia/Kolkata')
print(utc_raw)
