def sum_digits(n):
    if n == 0:
        return 0
    return (n % 10) + sum_digits(n // 10)

n = int(input("please enter the number: "))
print(sum_digits(n))
