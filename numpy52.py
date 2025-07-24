import numpy as np
num1=10
num2=13
print("numbers are ",num1,num2)
print("and btw them is",np.bitwise_and(num1,num2))
print("or btw them is",np.bitwise_or(num1,num2))
print("xor btw them is",np.bitwise_xor(num1,num2))
print("invert (bitwise not of the)",num1,"is",np.invert(num1))
print("bitwise left shift of",num1,"is",np.left_shift(num1,2))
print("bitwise right shift of",num2,"is",np.right_shift(num2,2))
print("binary representation of",num1,"is",np.binary_repr(num1))
print("binary representation of",num2,"is",np.binary_repr(num2))
