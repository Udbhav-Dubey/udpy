age_input=input("enter your age please : ")
age=int(age_input)

if(age<0):
    print("enter a valid age")
if(age >0 and age <18):
    print("minor")
elif(18<=age<=65):
    print("adult")
elif(age>65):
    print("boomer")

