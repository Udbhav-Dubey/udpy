a=[1,2,3,4,5,6]
res=[val for val in a if val %2==0]
print(res)

a=[i for i in range(1,11)]
print(a)

b=[(x,y) for x in range(3) for y in range(5)]
print(b)

mat=[[1,2,3],[11,12,13],[33,32,31]]
res=[val for row in mat for val in row ]
print(res)
