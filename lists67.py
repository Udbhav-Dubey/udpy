a=[[4,3,5],[1,2,5],[3,7,11]]
b=[[1,3],[9,3,5,7],[8]]
c=[x+y for x,y in zip(a,b)]
print(c)
d=list(map(lambda x:x[0]+x[1],zip(a,b)))
print(d)
for i in range(len(a)):
    a[i].extend(b[i])
print(a)
