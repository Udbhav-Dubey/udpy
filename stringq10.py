#Exercise 10: Write a program to count occurrences of all characters within a string
str1=input("please enter the string : ")
char_dict=dict()
for char in str1:
    if char in char_dict:
        char_dict[char]+=1
    else:
        char_dict[char]=1
print("result : ",char_dict)
