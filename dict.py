d={1:'geeks',2:'for',3:'geeks'}
print(d)
d1=dict(a="y2j",b="problem",c="is here")
print(d1)
print(d1["a"])
print(d[1])
print(d1.get("b"))
print(d.get("for"))
d["age"]=22
d[1]="nerds"
print(d)
del d[1]
print(d)
val=d.pop(2)
print(val)
key,val=d.popitem()
print(key,val)
d.clear()
print(d)
for key in d1:
    print(key)
for value in d1.values():
    print(value)

for key,value in d1.items():
    print(key,value)
