tup=(10,5,20)
print("Value in tup[0] = ", tup[0])
print("Value in tup[1] = ", tup[1])
print("Value in tup[2] = ", tup[2])
print("Value in tup[-1] = ", tup[-1])
print("Value in tup[-2] = ", tup[-2])
print("Value in tup[-3] = ", tup[-3])

for x in tup :
    print(x,end=" ")

tup2=('ten','five','twenty')
print("\n")
tup3=(tup,tup2)
print(tup3)
print(len(tup))
print(len(tup2))
print(len(tup3))
