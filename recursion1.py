#Recursion Practice #1: Print 1 to N (using recursion)
def func(i,num):
    print(i)
    if i==num:
        return 
    func(i+1,num)
num=int(input("enter the number : "))
func(1,num)

