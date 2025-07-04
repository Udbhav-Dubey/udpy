import pandas as pd
data = {"Name": ["Alice", "Bob"], "Age": [25, 30], "City": ["NY", "LA"]}
df=pd.DataFrame(data)
print(df)
if df["Age"].max()>22:
    print("old people")
    new_row = {"Name": "Frank", "Age": 20}
    df.loc[len(df)]=new_row
print(df)
