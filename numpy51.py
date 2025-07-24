import numpy as np
arr = np.array([[1, 2, 3], 
                [4, 9, 6], 
                [7, 8, 9]])
print(arr)
inverse_array = np.linalg.inv(arr)
print("Inverse array is ")
print(inverse_array)
print()

