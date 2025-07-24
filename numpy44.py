import numpy as np
arr1=np.eye(3)
arr=np.ones((3,3))*3
gfg=arr1.dot(arr)
print(gfg)
arr1= np.eye(3)
arr = np.ones((3, 3)) * 3
gfg = arr1.dot(arr).dot(arr)
print(gfg)
