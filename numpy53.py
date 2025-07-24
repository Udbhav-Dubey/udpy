import numpy as np
arr1=[2,8,125]
arr2=[3,15,165]
print("array:")
print(arr1)
print(arr2)
print("and bw them is ",np.bitwise_and(arr1,arr2))
print("or bw them is ",np.bitwise_or(arr1,arr2))
print("xor bw them is ",np.bitwise_xor(arr1,arr2))
print("invertion (bitwise not)of ",arr1,"is",np.invert(arr1))
print("left shift of ",arr1,"is ",np.left_shift(arr1,2))
print("right shift of",arr2,"is",np.right_shift(arr2,2))
for i in arr1:
    print("binary representation of",i,"is",np.binary_repr(i))
for i in arr2:
    print("binary representation of",i,"is",np.binary_repr(i))
