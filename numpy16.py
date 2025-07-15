import numpy as np
arr=np.array([2,4,6,8,10])
v=arr.view()
print("original id:",id(arr))
print("view id :",id(v))
arr[0]=12
print("original : ",arr)
print("view array : ",v)
c=arr.copy()
arr[0]=24
print("original id :",id(arr))
print("original id :",id(c))
print("original : ",arr)
print("copy array : ",c)
