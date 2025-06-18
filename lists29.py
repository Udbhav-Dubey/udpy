import operator as op
a=[10,20,30,40,50]
b=[1,3,4]
getter=op.itemgetter(*b)

res=getter(a)
print(res)  
