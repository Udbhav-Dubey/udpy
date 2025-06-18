import itertools
num=[1,2,3]
color=['red','blue','black']
value=[255,256]
for (a,b,c) in itertools.zip_longest(num,color,value):
    print(a,b,c)
