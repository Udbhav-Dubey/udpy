'''Exercise 9: Copy Specific Elements From Tuple

Write a program to copy elements 44 and 55 from the following tuple into a new tuple.'''
tuple1 = (11, 22, 33, 44, 55, 66)
tuple2=(tuple1[tuple1.index(44)],tuple1[tuple1.index(55)])
print(tuple2)
