import pandas as pd
import numpy as np
values_list = [[1.5, 2.5, 10.0], [2.0, 4.5, 5.0], [2.5, 5.2, 8.0],
               [4.5, 5.8, 4.8], [4.0, 6.3, 70], [4.1, 6.4, 9.0],
               [5.1, 2.3, 11.1]]
df=pd.DataFrame(values_list,columns=['Field_1','Field_2','Field_3'],index=['a','b','c','d','e','f','g'])
print(df)
df=df.apply(lambda x: np.square(x) if x.name in ['b','f']else x , axis=1)
df=df.assign(Product = lambda x : (x['Field_1']*x['Field_2']*x['Field_3']))
print(df)
