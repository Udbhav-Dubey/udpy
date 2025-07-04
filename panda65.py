import pandas as pd
data2 = {'Name':['Jai', 'Anuj', 'Jai', 'Princi', 
                 'Gaurav', 'Anuj', 'Princi', 'Abhi'], 
        'Age':[27, 24, 22, 32, 
               33, 36, 27, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj',
                   'Jaunpur', 'Kanpur', 'Allahabad', 'Aligarh'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd',
                         'B.Tech', 'B.com', 'Msc', 'MA'],
        'Score':[23, 34, 35, 45, 47, 50, 52, 53]}
df=pd.DataFrame(data2)
print(df)
grp2=df.groupby('Name')
sc=lambda x : (x-x.mean())/x.std()
print(grp2['Age'].transform(sc))
print(grp2)
grp3=df.groupby('Name')
print(grp3.filter(lambda x:len(x)>=2))
df.groupby('Name').agg({'Age': 'sum'})

