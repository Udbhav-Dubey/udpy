import pandas as pd
time_stamp_obj=pd.Timestamp('2015-06-26 07:35:00', tz='Asia/Kolkata')
print("TimeStamp object : ",time_stamp_obj)
iso=time_stamp_obj.isoformat()
print("iso format : ",iso)
print(time_stamp_obj.date())
print(time_stamp_obj.month)
