#Exercise 16: Removal all characters from a string except integers
str1 = 'I am 25 years and 10 months old'
res="".join([item for item in str1 if item.isdigit()])
print(res)
