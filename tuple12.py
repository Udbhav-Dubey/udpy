a,b,c=(100,200,300)
print(a)
print(b)
print(c)
a,_,c=(1,2,3)
print(a)
print(c)
#print(_)
a,*b,c=(11,12,13,14,15,16,17)
print(a)
print(b)
print(c)

nested_tup=(1,(2,3),4)
a,(b,c),d=nested_tup
print(a)
print(b)
print(c)
print(d)

def add(*args):
    return sum(args)
print(add(1,2,3,4))

def add(a,b,c):
    return a+b+c
nums=(1,2,3)
print(add(*nums))
