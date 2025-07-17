import numpy as np
a=np.arange(0,12).reshape(4,3)
print("original array:\n",a)
a[:,[0,2]]=a[:,[2,0]]
print("swapped\n",a)
i,j=0,2
a=a[:,[j if x==i else i if x==j else x for x in range(a.shape[1])]]
print(a)
col_order = [j if x == i else i if x == j else x for x in range(a.shape[1])]
res = np.take(a, col_order, axis=1)
print("After swapping:\n", res)
res = res.copy()
res[:, [0, 2]] = res[:, [2, 0]]
print("After swapping:\n", res)
