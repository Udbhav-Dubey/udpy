import pandas as pd
df=pd.read_csv("people_data.csv",nrows=3)
print(df)
df=pd.read_csv("people_data.csv",skiprows=[4,5])
print(df)
df=pd.read_csv("people_data.csv",skiprows=[2,4])
print(df)
df=pd.read_csv("people_data.csv",parse_dates=["Date of birth"])
print(df.info())
url = "https://media.geeksforgeeks.org/wp-content/uploads/20241121154629307916/people_data.csv"
df = pd.read_csv(url)
print(df)
