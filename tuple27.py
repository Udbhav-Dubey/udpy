l=[5,4,2,5,6,1]
res=[]
for i in range(len(l)):
    res.append((l[i],i))
print(res)

res2=[]
for index,element in enumerate(l):
    res2.append((element,index))

print("list of tuples")
print(res2)

l1=[1,2,3,4,4,5,6,4]
l2=[4,4,5,3,4,6,73,5,7]
l3=list(zip(l1,l2))
print(l3)
