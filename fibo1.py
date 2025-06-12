def fibo(n):
    if n==0 :
        return 0;
    elif n==1:
        return 1;
    else :
        return fibo(n-1)+fibo(n-2)

n=int(input("enter the number :"))
for i in range (0,n):
    print(fibo(i))
