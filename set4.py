set1={6,7,8,9,10}
print(set1)
set2={1,2,3,4,5}
set1.update(set2)
print("new set : ",set1)

set3={11,12,13,14,15}
set1|=set3
print("new set : ", set1)

set4={16,17,18,19,20}
from functools import reduce 

result_set = reduce(lambda res, ele: res.union(set([ele])), set4, set1)
print(result_set)
