import numpy as np
a=np.array([1,2,3,4,5])
b=np.array([2,4,6,7])
print(a)
print(b)
res=np.union1d(a,b)
print(res)
c=np.concatenate((a,b))
res=np.unique(c)
print(res)
res=np.array(list(set(np.concatenate((a,b)))))
res.sort()
print(res)
import numpy as np
from functools import reduce

a = [
    np.array([1, 2, 3]),
    np.array([3, 4, 5]),
    np.array([5, 6, 7]),
    np.array([0, 2, 4])
]

res = reduce(np.union1d, a)
print(res)
