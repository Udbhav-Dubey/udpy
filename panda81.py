import pandas as pd
import numpy as np
first =[1, 2, np.nan, 5, 6, 3, np.nan, 7, 11, 0, 4, 8]
second =[5, 3, 2, np.nan, 1, 3, 9, 21, 3, np.nan, 1, np.nan]
s1=pd.Series(first) 
s2=pd.Series(second)
result=s1.combine(s2,func=(lambda x1,x2:x1 if x1>x2 else x2),fill_value=5)
print(result)
