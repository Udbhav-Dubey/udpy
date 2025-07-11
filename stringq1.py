# Exercise 1A: Create a string made of the first, middle and last character
str1="jamie"
print(str1)
mid=int(0+(len(str1)-1)/2)
str2=str1[0]+str1[mid]+str1[len(str1)-1]
print(str2) 
#Exercise 1B: Create a string made of the middle three characters
str3=str1[mid-1]+str1[mid]+str1[mid+1]
 
print(str3)
