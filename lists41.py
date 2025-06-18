import itertools
num=[1,2,3]
color=['red','blue','black']
value=[255,256]
for (a,b,c) in itertools.zip_longest(num,color,value,fillvalue=-1):
    print(a,b,c)
