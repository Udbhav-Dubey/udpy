'''Exercise 12: Comparing Tuples
Compare two tuples and find out which one is “greater” and why?'''
t1 = (1, 2, 3)
t2 = (1, 2, 4)

print(f"Tuple 1: {t1}")
print(f"Tuple 2: {t2}")

if t1 > t2:
    print(f"{t1} is greater than {t2}")
elif t1 < t2:
    print(f"{t1} is less than {t2}")
else:
    print(f"{t1} is equal to {t2}")
