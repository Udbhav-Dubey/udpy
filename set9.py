s1={21,10,5,11,12}
s2={5,10,21,55,66}
s3={66,5,21,4,6,7,8}
print(s1&s2&s3)

test_list = [{5, 3, 6, 7}, {1, 3, 5, 2}, {7, 3, 8, 5}, {8, 4, 5, 3}]

print("The original list is : " + str(test_list))

res = set.intersection(*test_list)

print("Intersected Sets : " + str(res))

from operator import and_
from functools import reduce

test_list = [{5, 3, 6, 7}, {1, 3, 5, 2}, {7, 3, 8, 5}, {8, 4, 5, 3}]

print("The original list is : " + str(test_list))

res = set(reduce(and_, test_list))

print("Intersected Sets : " + str(res))
