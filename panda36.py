import pandas as pd

df = pd.read_csv("nba.csv")
print(df)
print(df.select_dtypes(include='number').sem(axis=0))
print(df.select_dtypes(include='number').sem(axis = 1))
