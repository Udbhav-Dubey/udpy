from collections import Counter as ctr

tup=(5,3,4,5,6,4,2,5,6,7,3,2,1)
print(tup)
res=tuple(ctr(tup).keys())
print(res)

