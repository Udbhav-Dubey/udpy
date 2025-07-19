'''Exercise 1: Perform basic dictionary operations

Given:

my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}

Perform following operations on given dictionary

    Add New Key-Value Pair: Add a new key-value pair, 'profession': 'Doctor', to the dictionary and print the updated dictionary.
    Modify Value: Change the value of the age key to 40 in the dictionary and print the updated dictionary.
    Access Key: Print the value associated with the city key.
'''
my_dict = {'name': 'Alice', 'age': 35, 'city': 'New York'}
print(my_dict)
my_dict['profession']='Doctor'
print(my_dict)
my_dict['age']=40
print(my_dict)
print(my_dict['city'])
