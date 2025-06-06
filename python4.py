a=12
b=1.1
print("a is ",a,"b is",b,"sum of a and b is",a+b)
a=33
c=a+b
print(a,b,c)
#now fstrings so we can use inside ""
print(f"{a} + {b} is {a+b} and c is sum :{c}")
#.format
print("{} + {} is {} and c is sum : {}".format(a,b,a+b,c))
