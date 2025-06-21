import numpy as np
test_tup = (7, 8, 9, 1, 10, 7)
test_array = np.array(test_tup)
print("The original tuple is : " + str(test_tup))
res = np.sum(test_array)
print("The summation of tuple elements are : " + str(res))
