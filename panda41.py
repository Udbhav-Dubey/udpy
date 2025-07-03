import pandas as pd
values_list = [[15, 2.5, 100], [20, 4.5, 50], [25, 5.2, 80],
               [45, 5.8, 48], [40, 6.3, 70], [41, 6.4, 90],
               [51, 2.3, 111]]
df=pd.DataFrame(values_list,columns=['Field_1','Field_2','Field_3'])
print(df)
df=df.assign(Product=lambda x :(x['Field_1']*x['Field_2']*x['Field_3']))
print(df)
