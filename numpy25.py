import numpy as np
a=np.array([1,2])
b=np.array([3,4])
res=np.concatenate((a,b))
print(res)
print(np.hstack((a,b)))
print(np.vstack((a,b)))
print(np.dstack((a,b)))
print("stack only :")
c=np.array([1,2,3,4])
d=np.array([11,12,13,14])
print(np.stack((c,d),axis=1))
b1 = np.array([[1, 1], [1, 1]])
b2 = np.array([[2, 2, 2], [2, 2, 2]])
b3 = np.array([[3, 3], [3, 3], [3, 3]])
b4 = np.array([[4, 4, 4], [4, 4, 4], [4, 4, 4]])
res=np.block([
    [b1,b2],
    [b3,b4]
])
print(res)
