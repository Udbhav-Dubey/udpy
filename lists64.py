import numpy as np
a=[1,2,3]
b=['a','b','c']
a=np.array(a,dtype=str)
b=np.array(b,dtype=str)
result = np.char.add(a, b)
print(result)
