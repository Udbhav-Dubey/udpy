from itertools import chain 
a=[1,2,3]
b=[4,5,6]
c=a+b
print(c)
aa=[1,2,3]
aa.extend(b)
print(aa)
e=[*a,*b]
print(c)
res=[]
for val in a:
    res.append(val)
for val in b:
    res.append(val)
print(res)
f=[item for item in a]+ [item for item in b]
print(f)
g=list(chain(a,b))
print(g)
