#✅ Problem #10: Recursively Count Digits of a Number
def count(num,ctr):
    if num==0:return ctr
    return count(num//10,ctr+1)

num=int(input("please enter the number : "))
ctr=0
print(count(num,ctr))
