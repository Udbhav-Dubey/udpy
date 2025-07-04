#Exercise 6: Count the total number of digits in a number
num=int(input("please enter the number :"))
lst=[int(digit) for digit in str(num)]
print(len(lst))
