import pandas as pd
timestamp=pd.Timestamp("2025-07-7 12:30:45")
print(timestamp)
unix_time=timestamp.timestamp()
print(unix_time)
timestamp2=pd.Timestamp("1975-01-04 00:03:30",tz="Asia/Kolkata")
print(timestamp2.timestamp())

