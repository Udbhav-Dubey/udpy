from operator import length_hint
a=[1,2,3,4,5]
print(len(a))
c=0
for val in a:
    c+=1
print(c)
print(length_hint(a))
