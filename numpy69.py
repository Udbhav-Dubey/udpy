import numpy as np
arr=np.array([[1,2,3],[4,5,6]])
result=np.swapaxes(arr,axis1=0,axis2=1)
print(arr)
print(result)
arr=np.random.rand(2,3,4)
result=np.swapaxes(arr,axis1=0,axis2=1)
print(arr)
print(result)
