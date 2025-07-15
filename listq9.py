#Exercise 9: Create a copy of a list
#Create a copy of a list [10, 20, 30] and modify the copy. Print both the original and the copied list to demonstrate they are independent.
list1=[10,20,30]
copied=list1[::]
print(copied)
list1[1]=200
print(copied)
print(list1)
copied.append(200)
print(copied)
print(list1)
