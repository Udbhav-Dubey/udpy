import pandas as pd
df=pd.read_csv("nba.csv")
print(df[:10])
result=df.select_dtypes(include='number').aggregate(['sum','min'])
print(result)
result=df.aggregate({"Number":['sum', 'min'], 
              "Age":['max', 'min'], 
              "Weight":['min', 'sum'],  
              "Salary":['sum']})
print(result)
