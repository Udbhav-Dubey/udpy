#✅ Recursion Problem #9: Find the K-th Fibonacci Number
def fibo(n):
    if n==1 :   return 1 
    elif n==0 :   return 0
    else : return fibo(n-1)+fibo(n-2)
num=int(input("please enter the kth number : "))
print(fibo(num))
