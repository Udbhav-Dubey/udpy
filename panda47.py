import pandas as pd
df = pd.DataFrame({'Weight':[45, 88, 56, 15, 71],
                   'Name':['Sam', 'Andrea', 'Alex', 'Robin', 'Kia'],
                   'Age':[14, 25, 55, 8, 21]})
index_ = pd.date_range('2010-10-09 08:45', periods = 5, freq ='H')
df.index=index_
print(df)
result=df.truncate(before='2010-10-09 09:45:00',after='2010-10-09 11:45:00')
print(result)
