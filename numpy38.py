import numpy as np
import numpy.matlib
outmat=np.matlib.empty((2,3))
print("output matrix \n ",outmat)
outmat=np.matlib.empty((2,3),dtype=int,order='C')
print("output matrix order =c\n ",outmat)
