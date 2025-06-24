a={1,2,3,4,5}
l=len(a)
print(l)

c=0
for i in a:
    c+=1

print(c)
length=sum(1 for _ in a) 
print(l)

for index,_ in enumerate(a):
    pass
l=index+1
print(l)
