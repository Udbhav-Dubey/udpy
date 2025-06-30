import pandas as pd
data=pd.read_csv("nba.csv")
print("Nba dataset (first 5 Rows) : ")
print(data.head())
print("now printing first 7 rows : ")
data=pd.read_csv("nba.csv")
top7=data.head(n=7)
print(top7)
print("printing only first 8 series : ")
series=data["Name"]
top=series.head(n=8)
print(top)
print("printing first 4 salaries : ")
salaries=data["Salary"]
print(salaries.head(n=4))
