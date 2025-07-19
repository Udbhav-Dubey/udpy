'''Exercise 3: Dictionary from Lists

Write a Python program to convert two Python lists into a dictionary where elements from the first list become keys and elements from the second list become values.
'''
keys = ['Ten', 'Twenty', 'Thirty']
values = [10, 20, 30]
res_dict=dict(zip(keys,values))
print(res_dict)
