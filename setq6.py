#Exercise 6: Add a list of Elements to a Set
sample_set = {"Yellow", "Orange", "Black"}
sample_list = ["Blue", "Green", "Red"]
sample_set.update(set(sample_list))
print(sample_set)
