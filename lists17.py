import itertools
r1=0
r2=10
li=list(itertools.islice(itertools.count(r1),r2-r1))
print(li)
