#Exercise 7: Find the number of occurrences of a substring in a string Write a Python code to find how often the substring “Emma” appears in the given string.
s=input("enter the string : ")
s=s.split()
ctr=0
for i in s :
    if (i=='Emma') : ctr+=1
print(ctr)
