# Product of Digits of a Number?
def product(num):
    if (num==0):return 0
    if (num<10):return num
    return num%10*product(num//10)
number=int(input("please enter the number : "))
print(product(number))
