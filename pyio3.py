#Exercise 3: Display Decimal Number to Octal using print() function
num=int(input("please enter the number : "))
print(num)
print(format(num, 'b'))   # Binary: '101010'
print(format(num, 'o'))   # Octal:  '52'
print(format(num, 'x'))   # Hex:    '2a'
print(format(num, 'X'))   # Hex (uppercase): '2A'
