#Exercise 12: Display Fibonacci series up to 10 terms
a=0
b=1
c=a+b
for i in range(0,10):
    print(a,end=" ")
    c=a+b
    a=b
    b=c
