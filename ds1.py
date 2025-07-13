'''Exercise 1: List Creation using two lists
Write a code to create a new list using odd-indexed elements from the first list and even-indexed elements from the second
Given two lists, l1 and l2, write a program to create a third list l3 by picking an odd-index element from the list l1 and even index elements from the list l2.'''

l1 = [3, 6, 9, 12, 15, 18, 21]
l2 = [4, 8, 12, 16, 20, 24, 28]
l3=[]
for index,i in enumerate(l1):
    if index%2!=0 : l3.append(i)
for index,i in enumerate(l2):
    if index%2==0 : l3.append(i)

print(l3)
