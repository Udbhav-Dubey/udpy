tup=(1,2,3,4,5)
print(tup)
temp=list(tup)
temp.clear()
tup=tuple(temp)
print(tup)

tup=(1,2,3,4)
tup=()
print(tup)

tup=(1,5,3,6,7)
tup=tup*0
print(tup)

tup=(1,5,6,7)
temp=tup[0:0]+()
print(temp)

del tup

print(tup)
