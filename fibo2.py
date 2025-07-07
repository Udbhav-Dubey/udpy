def fibo(n,memo={}):
    if n in memo:
        return memo[n]
    if n==0:
        return 0
    if n==1:
        return 1
    memo[n]=fibo(n-1,memo)+fibo(n-2,memo)
    return memo[n]

n=int(input("enter the kth number : "))
print(fibo(n))
