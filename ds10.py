#Exercise 10: remove duplicates from a list
#Write a code to remove duplicates from a list and create a tuple and find the minimum and maximum number
sample_list = [87, 45, 41, 65, 94, 41, 99, 94]
print(sample_list)
print(list(set(sample_list)))
t=tuple(set(sample_list))
print(t)
print(max(t))
print(min(t))
