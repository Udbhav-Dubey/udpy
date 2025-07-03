import pandas as pd
data = {'Name': ['Pandas', 'Geeks', 'for', 'Geeks'],
        'Height': [1, 2, 3, 4],
        'Qualification': ['A', 'B', 'C', 'D']}
df=pd.DataFrame(data,columns=['Name','Height','Qualification'])
print(data)
address=['HR','KA','PB','UP']
df['address']=address
print(df)
df = df.assign(address_2 = ['NewYork', 'Chicago', 'Boston', 'Miami'])
print(df)
address_3 = {'Pandas': 'Delhi', 'Geeks': 'Bihar', 
                'for': 'Noida', 'Geeks_2': 'Ranchi'}
df['address_3']=df['Name'].map(address_3)
print(df)
new_columns = {'Age': [21, 22, 23, 24], 
               'City': ['NY', 'LA', 'SF', 'DC']}
df=df.assign(**new_columns)
print(df)
