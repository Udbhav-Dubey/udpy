a=["y2j","problem"]
b="is here"
res=tuple(a)+ (b,)
print(res)

res1=(*a,b)
print(res1)
print(type(res1))

from itertools import chain 
res2=tuple(chain(a,[b]))
print(res2)

a.append(b)
res3=tuple(a)
print(res3)
