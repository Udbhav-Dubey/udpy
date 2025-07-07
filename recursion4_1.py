#m2
def func(n):
    if (n==0):
        return 0

    return n+func(n-1)

num=int(input("please enter the number : "))
print(func(num))
