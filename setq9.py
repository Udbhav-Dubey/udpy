'''Exercise 9: Check Subset
Check if set1 is a subset of set2. Write a code to return True if every element in the subset_set is also present in the main_set.'''
subset_set = {10, 20}
main_set = {10, 20, 30, 40}
if main_set.intersection(subset_set)==subset_set:
    print("subset")
else : print("not a subset")
