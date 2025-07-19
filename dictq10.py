#Exercise 10: Initialize dictionary with default values
employees = ['Kelly', 'Emma']
defaults = {"designation": 'Developer', "salary": 8000}
res=dict.fromkeys(employees,defaults)
print(res)
print(res["Kelly"])
