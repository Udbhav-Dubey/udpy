#🧩 Recursion Problem #2: Print N to 1
def func(num):
    print(num)
    if (num==1):
        return 
    func(num-1)
num=int(input("enter the number : "))
func(num)
