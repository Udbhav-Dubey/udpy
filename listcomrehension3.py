a=[1,2,3,4,5]
print(a)
result=[x*2 for x in a[:3]]
print(result)

a=[1,2,3,4,5,6,7,8]
print(a)
evens=[x for x in a[-3:] if x%2==0]
print(evens)

print(a)
squared=[x**2 for x in a[::2]]
print(squared)

a=[[1,2],[3,4],[5,6]]
print(a)
b=[y for row in a[:2] for y in row]
print(b)
