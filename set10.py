a=set("udbhav")
for i in a:
    print(i,end=" ")

print("\nnew: ")
for i in a.__iter__():
    print(i,end=" ")

print("\nnew: ")
for i in iter(a):
    print(i,end=" ")

print("\nnew: ")
for idx,i in enumerate(a):
    print(i,end=" ")
