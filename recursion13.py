#13: gcd 
def gcd(a,b):
    if (b==0):
        return a
    return gcd(b,a%b)
a=int(input("please enter a : "))
b=int(input("please enter b : "))

if (a<b):
    temp=a
    a=b
    b=temp
print(gcd(a,b))
