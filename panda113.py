import pandas as pd
nme = ["aparna", "pankaj", "sudhir", "Geeku"]
deg = ["MBA", "BCA", "M.Tech", "MBA"]
scr = [90, 40, 80, 98]
dict={'Name':nme,'Degree':deg,'score':scr}
df=pd.DataFrame(dict)
print(df)
df.to_csv("file2.csv",header=False,index=False)
# df.to_csv(r'C:\Users\Admin\Desktop\file3.csv')
import numpy as np
users = {'Name': ['John', 'Cody', 'Drew'],
    'Age': [20,21,25]}
df = pd.DataFrame(users, columns=['Name','Age'])
print("Original DataFrame:")
print(df)
print('Data from Users.csv:')
df.to_csv('Users.csv', sep='\t', index=False,header=True)
new_df = pd.read_csv('Users.csv')
print(new_df)

