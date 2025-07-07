import pandas as pd
df=pd.read_csv("nba.csv")
df.head(10)
new_row = pd.DataFrame({'Name':'Geeks', 'Team':'Boston', 'Number':3,
                        'Position':'PG', 'Age':33, 'Height':'6-2',
                        'Weight':189, 'College':'MIT', 'Salary':99999},
                                                            index =[0])
df = pd.concat([new_row, df]).reset_index(drop = True)
print(df.head(5))
new_row1 = pd.DataFrame({'Name':'hhee', 'Team':'iki', 'Number':3,
                        'Position':'LL', 'Age':3, 'Height':'2',
                        'Weight':89, 'College':'iIT', 'Salary':99999},
                                                            index =[0])
df = pd.concat([new_row1, df[:]]).reset_index(drop = True)
print(df.head(5))

