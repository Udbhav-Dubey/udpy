import pandas as pd
import numpy as np
data1 = {'Name':['Jai', 'Anuj', 'Jai', 'Princi',
                 'Gaurav', 'Anuj', 'Princi', 'Abhi'],
        'Age':[27, 24, 22, 32,
               33, 36, 27, 32],
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj',
                   'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd',
                         'B.Tech', 'B.com', 'Msc', 'MA']}
df=pd.DataFrame(data1)
print(df)
df.groupby('Name')
print(df.groupby('Name').groups)
grp1=df.groupby('Name')
result=grp1['Age'].aggregate(np.sum)
print(result)
grp2=df.groupby(['Name','Qualification'])
result=grp2['Age'].aggregate(np.sum)
print(result)
grp3 = df.groupby('Name')
result3=grp3['Age'].agg([np.sum, np.mean, np.std])
print(result3)

