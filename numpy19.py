import numpy as np
arr=np.array([1,8,3,4,5])
print("original array : ",arr)
arr=np.append(arr,[7])
print(arr)
arr1=np.array([55,66,77])
print("arr1:",arr1)
arr=np.append(arr,arr1)
print(arr)
arr2=np.array([10,11,12,13])
print("arr2:",arr2)
arr=np.concatenate((arr,arr2))
print(arr)
arr3=np.array([19.12,20.6])
print("arr3:",arr3)
arr=np.append(arr,arr3)
print(arr)
