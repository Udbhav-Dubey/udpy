#Exercise 4: Remove first n characters from a string Write a Python code to remove characters from a string from 0 to n and return a new string.
str=input("enter the string : ")
n=int(input("enter the n till which char to be removed : "))
nstr=str[n:]
print(nstr)
