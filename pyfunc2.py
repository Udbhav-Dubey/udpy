'''Exercise 2: Create a function with variable length of arguments

Write a program to create a function func1() that accepts a variable number of arguments and prints each of their values.

Note: Create this function so that it can receive any number of arguments, process them, and display the value of each individual argument.'''

def func1(*args):
    for arg in args:
        print(arg)

func1("ud",19,2.2)
