#Exercise 9: Check Palindrome Number Write a Python code to check if the given number is a palindrome. A palindrome number reads the same forwards and backward. For example, 545 is a palindrome number.
number=int(input("enter the number : "))
rev=int(str(number)[::-1])
if number==rev : print("palindrome")
else : print("not a palindrome ")

