'''Exercise 15: Map Tuples
Given a tuple of numbers, create a new tuple where each number is squared.'''
t = (1, 2, 3, 4)
t2=tuple(map(lambda x: x*x,t))
print(t2)
