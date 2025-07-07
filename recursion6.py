# Problem #6: Factorial using recursion?
def func(n):
    if (n==1 or n==0):
        return 1
    return n*func(n-1)
num=int(input("please enter the number : "))
print(func(num))
