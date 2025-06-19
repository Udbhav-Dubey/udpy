a=[1,2,4,5,6,7,2,4,5]
print(a)
idx=2
a=[item for i ,item in enumerate(a) if i!=idx]
print(a)
del a[idx]
print(a)
a.remove(a[idx])
print(a)
a.pop(idx)
print(a)
a.clear()
print(a)
#or 
a=[1,2,3,4,5,6]
print(a)
del a[:]
print(a)
