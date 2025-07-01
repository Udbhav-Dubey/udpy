#Exercise 22: Capitalize the first letter of each word in a string
s=input("enter the string : ")
words=s.split()
capatilised=[]
for word in words:
    capatilised.append(word[0].upper()+word[1:])
result=' '.join(capatilised)
print(result)
