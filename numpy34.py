import numpy as np
a=np.array([1,2,2,3,4,5,5,6])
res=np.unique(a)
print(res)
res,count=np.unique(a,return_counts=True)
print("res:",res)
print("count:",count)
import numpy as np
a = np.array([3, 1, 2, 1])
unique, inverse = np.unique(a, return_inverse=True)
print("Unique:", unique)
print("Inverse:", inverse)
import numpy as np
a = np.array([4, 3, 3, 2, 1, 2])
unique, indices = np.unique(a, return_index=True)
print("Unique:", unique)
print("Indices:", indices)
