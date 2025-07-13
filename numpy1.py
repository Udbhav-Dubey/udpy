import numpy as np
arr=np.array([1,2,3])
print(arr)
arr=np.array([[1,2,3],
             [4,5,6]])
print(arr)
arr=np.array((1,3,2))
print(arr)
arr=np.array([[-1,2, 0, 4],
                [4, -0.5, 6, 0],
                [2.6, 0, 7, 8],
                [3, -7, 4, 2.0]])
arr2=arr[:2,::2]
print("first 2 rows and alternatives columsn(0and2):\n",arr2)
print(arr[1][1])
print(arr[0][0])
print(arr[2][2])
print(arr[3][3])

