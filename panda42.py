import pandas as pd
import numpy as np
values_list = [[15, 2.5, 100], [20, 4.5, 50], [25, 5.2, 80],
               [45, 5.8, 48], [40, 6.3, 70], [41, 6.4, 90], 
               [51, 2.3, 111]]
df=pd.DataFrame(values_list,columns=['Field_1','Field_2','Field_3'],
                index=['a','b','c','d','e','f','g'])
df=df.apply(lambda x:np.square(x) if x.name=='d' else x ,axis=1)
print(df)
df=df.apply(lambda x:np.square(x) if x.name in ['a','e','g'] else x ,axis=1)
print(df)
