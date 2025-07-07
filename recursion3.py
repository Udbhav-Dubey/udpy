# Recursion Problem #3: Print 1 to N using Backtracking Style
def func(n):
    if 1 > n:
        return
    func(n-1)
    print(n)

num = int(input("Enter the number: "))
func(num)

