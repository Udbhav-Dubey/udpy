'''
Exercise 2: Perform dictionary operations

Given:

my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}

Perform following operations on given dictionary

    Remove Key-Value Pair : Remove the profession key-value pair from the dictionary.
    Get Items (Key-Value Pairs): Print all key-value pairs (items) in the dictionary.
    Check if Key Exists in the dictionary
'''
my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York', 'profession': 'Doctor'}
print(my_dict)
del my_dict['profession']
print(my_dict)
for key,value in my_dict.items():
    print(key,value)
