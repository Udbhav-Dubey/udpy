d=dict( a =101, b =202, c =303)
print(d)
keys=['a','b','c']
values=[1,2,3]
d1={k : v for k,v in zip(keys,values)}
print(d1)

from collections import defaultdict
a=[('a',1),('b',2),('a',3),('c',4)]
d=defaultdict(list)
for key,value in a:
    d[key].append(value)

print(dict(d))

a = [('a', 1), ('b', 2), ('a', 3), ('c', 4)]
d = {} 

for key, val in a:
    d.setdefault(key, []).append(val)

print(d)

keys = ['p', 'q', 'r']
values = [5, 10, 15]

d = {} 
for i in range(len(keys)):
    d[keys[i]] = values[i]

print(d)

