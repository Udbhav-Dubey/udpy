import pandas as pd
data=pd.date_range('1/1/2011',periods=10,freq='h')
print(data)
x=pd.Timestamp.now()
print(x.month)
print(x.year)
print(x.hour)
print(x.minute)
print(x.weekday())
#us_now=x.tz_convert("UTC")
#print(us_now)
rng = pd.DataFrame()
rng['date'] = pd.date_range('1/1/2011', periods = 72, freq ='h')
print(rng[:5])
rng['year'] = rng['date'].dt.year
rng['month'] = rng['date'].dt.month
rng['day'] = rng['date'].dt.day
rng['hour'] = rng['date'].dt.hour
rng['minute'] = rng['date'].dt.minute
print(rng.head(3))
print(pd.Timestamp.now())
