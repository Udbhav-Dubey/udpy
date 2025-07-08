import pandas as pd
timestamp=pd.Timestamp('2013-12-04 15:30:47')
year=timestamp.year
print(year)
month=timestamp.month
print(month)
day=timestamp.day
print(day)
hour=timestamp.hour
print(hour)
minute=timestamp.minute
print(minute)
weekday=timestamp.weekday()
print(weekday)
quarter=timestamp.quarter
print(quarter)
