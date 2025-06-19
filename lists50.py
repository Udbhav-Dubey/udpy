import numpy as np
a=[4,5,7,52,6,65,7,645,666,555]
arr=np.array(a)
indices=np.where(arr==7)[0]
print("indices",indices.tolist())
