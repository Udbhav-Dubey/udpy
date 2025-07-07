import pandas as pd
data1 = {'Name':['Jai', 'Princi', 'Gaurav'],
        'Age':[27, 24, 22]}
data2 = {'Address':['Allahabad', 'Kannuaj', 'Allahabad', 'Kanpur'],
        'Qualification':['MCA', 'Phd', 'Bcom', 'B.hons']}
df = pd.DataFrame(data1, index=pd.Index(['K0', 'K1', 'K2'], name='key'))
index = pd.MultiIndex.from_tuples([('K0', 'Y0'), ('K1', 'Y1'),
                                   ('K2', 'Y2'), ('K2', 'Y3')],
                                   names=['key', 'Y'])
df1 = pd.DataFrame(data2, index= index)
print(df, "\n\n", df1)
result=df.join(df1,how='inner')
print(result)
