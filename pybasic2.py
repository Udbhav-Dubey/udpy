#Exercise 3: Print characters present at an even index number Write a Python code to accept a string from the user and display characters present at an even index number
str=input ("enter the string : " )
for idx,i in enumerate(str):
    if idx % 2==0:
        print(i)
