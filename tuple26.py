a=[(1,3),(5,4)]
b=[]
for t in a:
    for val in t:
        b.append(val)
print(b)
c=[val for t in a for val in t ]
print(c)
from itertools import chain 
d=[chain(*a)]
print(d)
d=list(chain(*a))
print(d)
