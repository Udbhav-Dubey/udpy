tup=(1,2,3,4,5,6,7,2,6,7)
res=tuple(set(tup))
print(tup)
print(res)

tup=(1,2,3,4,5,6,7,2,6,7)
print(tup)
res2=[]
for i in tup:
    if i  not in res2:
        res2.append(i)
    res3=tuple(res2)

print(res3)


