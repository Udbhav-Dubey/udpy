#Exercise 13: Find the factorial of a given number
num=int(input("please enter the given number : "))
result=1
for i in range(num,1,-1):
    result*=i
print(result)
