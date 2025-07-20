'''Exercise 11: Function Returning Tuple
Write a function get_min_max(numbers) that takes a list of numbers and returns a tuple containing the minimum and maximum number.'''

def get_min_max(my_numbers):
    maxi=max(my_numbers)
    mini=min(my_numbers)
    tup=(maxi,mini)
    return tup

my_numbers = [10, 5, 20, 2, 15]
tup=get_min_max(my_numbers)
print(tup)
