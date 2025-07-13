#Exercise 7: Subset or Superset of another set
#Write a code to checks if one set is a subset or superset of another set. If found, delete all elements from that set.
first_set = {27, 43, 34}
second_set = {34, 93, 22, 27, 43, 53, 48}
print("first_set : ",first_set)
print("second_set : ",second_set)
print("first set is subset of second set -",first_set.issubset(second_set))
print("second set is subset of first set -",second_set.issubset(first_set))
if first_set.issubset(second_set):
    first_set.clear()
if second_set.issubset(first_set):
    second_set.clear()

print("first set ",first_set)
print("second set",second_set)

