age =int(input("enter the age : "))
if (age > 18 and age < 65):
    print("adult")
elif(age > 65):
    print("old")
else:
    print("minor")
