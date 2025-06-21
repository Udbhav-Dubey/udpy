tup=(10,4,5,6,7)
print(tup)
print(tup[0])
print(tup[-1])
print(tup[len(tup)-1])
from operator import itemgetter
res=itemgetter(0,-1)(tup)
print(" "+ str(res))
front,*_,rear=tup
res=(front,rear)
print(str(res))
print(tuple([front]))
print(tuple([rear]))
print(tuple([*_]))
