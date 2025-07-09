import pandas as pd
current_time=pd.Timestamp.now()
print("current timestamp: ",current_time)

timestamps=pd.date_range(end=pd.Timestamp.now(),periods=5,freq="D")
data={
    "Timestamp":timestamps,
    "Temperature":[21.2,23.2,27.5,25.1,22.4]
}
df=pd.DataFrame(data)
print(df)
