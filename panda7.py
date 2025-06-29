import pandas as pd
import numpy as np
ser=pd.Series()
print(ser)
data=np.array(['g','e','e','k','s'])
ser=pd.Series(data)
print(ser)
st='udbhav'
stl=list(st)
ser1=pd.Series(stl)
print(ser1)
data_dict = {'Geeks': 10, 'for': 20, 'geeks': 30}
ser2=pd.Series(data_dict)
print(ser2)

