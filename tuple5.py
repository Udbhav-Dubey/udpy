a=[1,2,3]
b=['apple','orange','cherry']
res=list(zip(a,b))
print(res)
print(type(res))
c=[[1,'one'],[2,'two'],[3,'three']]
res1=list(map(tuple,c))
print(res1)
res2=[(x,y) for x,y in zip(a,b)]
print(res2)
res3=[]
for i in range(len(a)):
    res3.append((a[i],b[i]))
print(res3)
