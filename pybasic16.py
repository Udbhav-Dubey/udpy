#Exercise 17: Generate Fibonacci series up to 15 termsHave you ever wondered about the Fibonacci Sequence? It’s a series of numbers in which the next number is found by adding up the two numbers before it. The first two numbers are 0 and 1.For example, 0, 1, 1, 2, 3, 5, 8, 13, 21. The next number in this series is 13 + 21 = 34.
a=0
b=1
c=0
for i in range(0,15):
    print(c)
    a=b
    b=c
    c=a+b
