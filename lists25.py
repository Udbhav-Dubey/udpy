a=[1,2,3,4,5]
b=['a','b','c','d','e','f']
for i , v in zip(range(len(a)),zip(a,b)):
    print(i,v)
