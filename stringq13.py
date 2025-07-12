'''Exercise 13: Split a string on hyphens
Write a program to split a given string on hyphens and display each substring.'''
str1 = "Emma-is-a-data-scientist"
str2=str1.split("-")
for char in str2:
    print(char)
