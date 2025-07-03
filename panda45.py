import pandas as pd
data = {'Name': ['Pandas', 'Geeks', 'for', 'Geeks'],
        'Height': [1, 2, 3, 4],
        'Qualification': ['A', 'B', 'C', 'D']}
df=pd.DataFrame(data)
df.insert(2,'Age',[21,23,25,27],True)
print(df)
df.loc[df['Height'] >= 3, 'Category'] = 'Tall'
df.loc[df['Height'] < 3, 'Category'] = 'Short'
print(df)
