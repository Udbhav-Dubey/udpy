import numpy as np
sequence=np.arange(10)
print("basic sequence :",sequence)
seq=np.arange(0,1,.2)
print(seq)
sequence=np.arange(0,100,7)
filtered=sequence[sequence>40]
print(filtered)
arr=np.zeros((3,4))
print(arr)
d=np.zeros((2,2),dtype=[('f','f4'),('i','i4')])
print(d)
e=np.zeros((2,3),order='C')
print(e)
f=np.zeros((2,3),order='F')
print(f)
