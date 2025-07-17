'''Exercise 5: Symmetric Difference
Find the symmetric difference of set1 and set2. Write a code to returns a new set containing elements that are unique to either set1 or set2, but not in both. It’s like finding the union and then removing the intersection.'''
set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
symmetric_difference_set = set1.symmetric_difference(set2)
print("Symmetric Difference:", symmetric_difference_set)
