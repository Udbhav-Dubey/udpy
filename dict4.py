d={'a':10,'b':20,'c':30}
print(d['a'])
print(d.get('b'))
print(d.get('d','key not found'))
print(list(d))
print(list(d.values()))
print(list(d.keys()))
for k in d:
    print(k)
for k,val in d.items():
    print(k,val)
for k in d.values():
    print(k)
if ("d" in d):
    print("exists")
else: print("nope")
