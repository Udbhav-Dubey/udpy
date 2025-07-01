#Exercise 15: Get an int value of base raises to the power of exponentWrite a function called exponent(base, exp) that returns an int value of base raises to the power of exp.INote here exp is a non-negative integer, and the base is an integer.
def exponent(base,exp):
    return base**exp

base=int(input("please enter the base : "))
expo=int(input("please enter the exponent: "))

print(exponent(base,expo))
