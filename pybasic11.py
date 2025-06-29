#Exercise 12: Calculate income tax Calculate income tax for the given income by adhering to the rules below axable Income	Rate (in %)
#First $10,000	0
#Next $10,000	10
#The remaining	20
money=int(input("enter the money pal : "))
if money <= 10000:
    tax=0
elif money <=20000:
    x=money-10000
    x=x*0.1
    tax=x
else :
    tax=0
    tax=10000*0.1
    tax+=(money-20000)*0.2

print("total tax to pay is",tax)
