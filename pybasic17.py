#leap year
year=int(input("please tell the year"))
if (year%4==0  and year%100!=0 and year%400==0):
    print("leap")
else :
    print("no leap")
