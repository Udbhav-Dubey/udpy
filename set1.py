s={1,2,3,4,5}
print(s)
fs=frozenset(s)
print("frozenset: ",end=" ")
print(fs)
s.add("add")
print(s)
print(fs)

for i in fs:
    print(i,end=" ");

print("\n")
print(2 in fs)
