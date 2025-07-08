import pandas as pd
timestamp = pd.Timestamp('2023-10-04 15:30:00')
time_period=pd.Period('2023-10-04',freq='M')
year=time_period.year
print(year)
month=time_period.month
print(month)
quarter=time_period.quarter
print(quarter)
data_offset=pd.DateOffset(years=2,months=3,days=10)
new_timestamp=timestamp+data_offset
print(new_timestamp)
# to print next 10

