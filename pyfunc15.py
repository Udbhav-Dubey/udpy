#Exercise 17: Use a lambda with the sorted() function to sort a list of tuples based on the second element
data = [('apple', 5), ('banana', 2), ('cherry', 8), ('date', 1)]
sorted=sorted(data,key=lambda item:item[1])
print(sorted)
