#Exercise 8: Format variables using string.format() method
totalMoney = 1000
quantity = 3
price = 450
statement = "I have {money} dollars so I can buy {qty} football for {cost:.2f} dollars."
print(statement.format(money=totalMoney, qty=quantity, cost=price))
