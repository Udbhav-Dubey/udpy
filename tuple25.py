a=(1,2,3)
b=(2,3,4)
c=a+b
print(c)
print(type(c))
d=sum((a,b),())
print(d)
temp_a=list(a)
temp_b=list(b)
temp_a.extend(temp_b)
e=tuple(temp_a)
print(e)
import itertools
f=tuple(itertools.chain(a,b))
print(f)
print(type(f))
a+=b
print(a)
