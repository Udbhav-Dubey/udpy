d={1:10,2:20,3:30}
d[4]=40
print(d)
d.update({5:50,6:60})
print(d)
a=[(7,70),(8,80)]
d.update(a)
print(d)
d.setdefault(9,90)
print(d)
d2={k:v*2 for k,v in d.items() if k >2}
print(d2)
for i in range(4, 6):
    d2[i] = i * 10  
    print(d2)
