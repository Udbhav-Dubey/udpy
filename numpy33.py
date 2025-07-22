import numpy as np
a=np.array([[1,2],[3,4],[1,2],[7,8]])
res=np.unique(a,axis=0)
print(res)
import numpy as np
a = np.array([[7, 8], [7, 9], [6, 8], [7, 8]])
s = np.lexsort(a.T[::-1])
a = a[s]

mask = np.ones(len(a), bool)
mask[1:] = np.any(np.diff(a, axis=0), axis=1)
res = a[mask]
print(res)
import numpy as np
a = np.array([[0, 0], [1, 1], [0, 0], [2, 2]])
res = np.array(list({tuple(r) for r in a}))
print(res)
import numpy as np
a = np.array([[1, 2, 3], [4, 5, 6], [1, 2, 3], [7, 8, 9]])
b = np.ascontiguousarray(a).view(np.dtype((np.void, a.dtype.itemsize * a.shape[1])))

_, idx = np.unique(b, return_index=True)
res = a[np.sort(idx)]
print(res)
