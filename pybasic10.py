#Exercise 11: Get each digit from a number in the reverse order. For example, If the given integer number is 7536, the output shall be “6 3 5 7“, with a space separating the digits.
number = int(input("please enter the number : "))
reverse=str(number)[::-1]
for i in reverse : 
    print(i,end=" ")

