'''Exercise 5: Display numbers from a list using a loop

Write a Python program to display only those numbers from a list that satisfy the following conditions

    The number must be divisible by five
    If the number is greater than 150, then skip it and move to the following number
    If the number is greater than 500, then stop the loop
'''
li=list(map(int,input("enter the elements").split()))
for i in range(0,len(li)):
    if (li[i]>150):continue
    if (li[i]>500):break
    if (li[i]%5==0):
        print(li[i])
    
