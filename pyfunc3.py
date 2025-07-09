'''Exercise 3: Return multiple values from a function

Write a function calculation() that accepts two variables and calculates both their addition and subtraction. The function should then return both the sum and the difference in a single return statement.'''

def func(n1,n2):
    return n1+n2,n1-n2

print(func(10,20))
