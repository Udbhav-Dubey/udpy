#Exercise 14: List Comprehension for Numbers
my_list = [1, 2, 3, 'Jessa', 4, 5, 'Kelly', 'Jhon', 6]
new=[x for x in my_list if isinstance(x,(int,float))]
print(new)
