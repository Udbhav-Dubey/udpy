#Exercise 16: Check Palindrome NumberA palindrome number is a number that remains the same when its digits are reversed. In simpler terms, it reads the same forwards and backward. For example 121, 5005.Write a code to check if given number is palindrome.
numb=int(input("enter the number : "))
rev1=int(str(numb)[::-1])
if (rev1 == numb ): 
    print("palindrome")
else :
    print("not a palindrome")
