#Exercise 17: Invert Dictionary
original_dict1 = {'a': 1, 'b': 2, 'c': 3}
inverted_dict={}
for key,values in original_dict1.items():
    inverted_dict[values]=key
print(inverted_dict)
