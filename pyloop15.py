'''Exercise 15: Print elements from a given list present at odd index positions

Given:
'''
my_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

for index,i in enumerate(my_list):
    if (index%2!=0):
        print(i)
   
