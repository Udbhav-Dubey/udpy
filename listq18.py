#Exercise 18: Concatenate two lists in the following order
list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
res=[i+j for i in list1 for j in list2]
print(res)
