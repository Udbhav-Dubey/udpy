s={1,2,3,4,5}
print(3 in s)
print(6 in s)
print(6 not in s)
print(3 not in s)

import operator as op
s={12,23,34,45,56}
print(op.countOf(s,23)>0)
print(op.countOf(s,67)>0)
