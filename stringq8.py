'''Exercise 9: Calculate the sum and average of the digits present in a string

Given a string s1, write a program to return the sum and average of the digits that appear in the string, ignoring all other characters.'''
str1 = "PYnative29@#8496"
ctr=0
sum=0

for i in str1:
    if i.isdigit():
        sum+=int(i)
        ctr+=1

print("sum is ",sum,"average is ",sum/ctr)
