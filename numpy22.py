import numpy as np
arr=np.arange(5*5).reshape(5,5)
print(arr)
print(arr.shape)
arr_5d = arr[np.newaxis, ..., np.newaxis, np.newaxis]
print(arr_5d.shape)
x=np.zeros((3,4))
y=np.expand_dims(x,axis=1).shape
print(y)
newaxis=(0,3,-1)
arr_5D=np.expand_dims(arr,axis=newaxis)
print(arr_5D.shape)
arr=np.arange(6)
arr_reshape=arr.reshape((2,3))
print(arr_reshape.shape)
