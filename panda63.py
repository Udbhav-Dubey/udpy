import pandas as pd
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
gk=df.groupby('Name')
print(gk)
print(gk.first())
df.groupby(['Name','Qualification'])
print(df.groupby(['Name','Qualification']).groups)
df.groupby('Name')['Age'].sum()
print((df.groupby('Name')['Age']).sum)
grp = df.groupby('Name')
for name, group in grp:
    print(name)
    print(group)
    print()
grp = df.groupby('Name')
grp.get_group('Jai')
grp = df.groupby(['Name', 'Qualification'])
grp.get_group(('Jai', 'Msc'))

