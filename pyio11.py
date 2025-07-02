#Exercise 11: Percentage Display
#Ask the user for a numerator and a denominator. Calculate the percentage and display it with two decimal places followed by a percent sign (e.g., 75.50%).
numerator=float(input("enter the numerator : "))
denominator=float(input("enter the denominator : "))
answer=(numerator/denominator)*100
print(f"{answer:.2f}%")
