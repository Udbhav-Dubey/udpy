import numpy as np
a=np.array(['geeks','for','geeksgeeks'])
print(a)
print(np.char.count(a,'geek'))
print(np.char.count(a,'fo'))
print(np.char.rfind(a,'geek'))
print(np.char.rfind(a,'fo'))
print(np.char.isnumeric(a))
print(np.char.isnumeric("123"))
