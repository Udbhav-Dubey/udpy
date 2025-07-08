#Exercise 17: Find the sum of a series of a number up to n terms
num=int(input("enter the num : "))
terms=int(input("enter the terms : "))
sum=0
for i in range(1,terms+1):
    sum+=num
    num=num*10+num

print(sum)
