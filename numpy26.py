import numpy as np
a=np.ma.array([1,2,3],mask=[0,1,0])
b=np.ma.array([4,5,6],mask=[0,0,1])
res=np.ma.concatenate([a,b])
print(res)
