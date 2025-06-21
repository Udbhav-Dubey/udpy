import numpy as np
test_list = [(0, 10), (11, 20), (21, 30), (31, 40), (41, 50)]
print("The original list is : " + str(test_list))
K = 37
arr = np.array(test_list)
idx = np.where((arr[:, 0] <= K) & (arr[:, 1] > K))[0][0]
print("The position of element: ", idx)
