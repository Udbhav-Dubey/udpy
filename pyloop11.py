'''Exercise 11: Print all prime numbers within a range

Note: A Prime Number is a number that can only be divided by itself and 1 without remainders (e.g., 2, 3, 5, 7, 11)

A Prime Number is a natural number greater than 1 that cannot be made by multiplying other whole numbers.

Examples:

    6 is not a prime number because it can be made by 2×3 = 6
    37 is a prime number because no other whole numbers multiply to make it.
'''
import math as mt
def primechecker(num):
    for i in range(2,int(mt.sqrt(num)):
        if (num%i==0) : return False
    return True

start=int(input("please enter the start point : "))
end=int(input("please enter the end point : "))
for num in range (start,end):
    if (primechecker(num)==1): print(num)


