#Exercise 21: Check if a user-entered string contains any digits using a for loop
string=input("please enter a string : ")
for i in string:
    if i>=0 and i <= 9 :
        print("contains a number ")
        break
    else : print("does not contain a number")
