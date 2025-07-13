#Exercise 6: Set Intersection and Removal
#Write a code to find the intersection (common) of two sets and remove those elements from the first set.
first_set = {23, 42, 65, 57, 78, 83, 29}
second_set = {57, 83, 29, 67, 73, 43, 48}
intersection=first_set.intersection(second_set)
print("intersection is : ",intersection)
for item in intersection:

    first_set.remove(item)
print(first_set)
