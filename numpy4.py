import numpy as np
x=np.array([1,2,3])
y=np.array([[1,2],[3,4]])
z=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(x,"\n")
print(y,"\n")
print(z,"\n")
print(z.shape)
print(z.dtype)
print(z.ndim)
xx=np.array([11,12,13])
print(x+xx)
yy=np.array([[1,2],[3,4]])
print(y+yy)
print(np.dot(x,xx))
print(np.dot(y,yy))
