#Exercise 5: Count all letters, digits, and special symbols from a given string
str1 = "P@#yn26at^&i5ve"
ctr_letter=0
ctr_digit=0
ctr_symbol=0
for char in str1:
    if char.isalpha():
        ctr_letter+=1
    if char.isdigit():
        ctr_digit+=1
    else :
        ctr_symbol+=1

print(ctr_letter)
print(ctr_digit)
print(ctr_symbol)
