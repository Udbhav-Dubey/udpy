a=["hello","world","python"]
a=[x*2 for x in a]

print(a)

a=["hello","world","python"]
a=list(map(lambda x: (x+" ")*3,a))

print(a)
