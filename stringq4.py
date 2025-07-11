#Exercise 4: Arrange string characters such that lowercase letters should come first
str1="PYnAtive"
print("original string",str1)
lower=[]
upper=[]
for char in str1:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)

sorted_str=''.join(lower+upper)
print(sorted_str)
