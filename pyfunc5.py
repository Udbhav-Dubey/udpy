'''Exercise 5: Create an inner function

Create a program with nested functions to perform an addition calculation as follows:

    Define an outer function that accepts two parameters, a and b.
    Inside this outer function, define an inner function that calculates the sum of a and b.
    The outer function should then add 5 to this sum.
    Finally, the outer function should return the resulting value.”
'''
def func1(a,b):
    def func2(a,b):
        return a+b
    result=func2(a,b)+5
    return result

print(func1(15,10))
