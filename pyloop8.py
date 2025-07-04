#Exercise 8: Print list in reverse order using a loop
li=list(map(int,input("enter the number seprated by space : ").split()))
print("using slicing : ",li[::-1])
for val in reversed(li):
    print(val)
