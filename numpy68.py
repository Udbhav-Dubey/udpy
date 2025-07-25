import numpy as np
arr=np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
print(arr)
print(arr.shape)
moved_arr=np.moveaxis(arr,0,2)
print("\narray after moveaxis:")
print(moved_arr)
print("shape of array after moveaxis:",moved_arr.shape)
arr = np.random.rand(2, 3, 4)

result = np.moveaxis(arr, source=[0, 1], destination=[1, 0])

print("Original shape:", arr.shape)
print(arr)
print("New shape:", result.shape)
print(result)
