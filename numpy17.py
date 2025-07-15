import numpy as np
arr=np.array([2,4,6,8,10])
nc=arr
print("original idea : ",id(arr))
print("assigned id   : ",id(nc))

nc[0]=12
print("original idea : ",arr)
print("assigned id :",nc)

c=arr.copy()
v=arr.view()
print(c.base)
print(v.base)
