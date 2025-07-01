#Exercise 20: Print Reverse Number Pattern
#Expected Output:
#1 1 1 1 1 
#2 2 2 2 
#3 3 3 
#4 4 
#5 
z=1
for i in range(5,0,-1):
    print(f"{z} " * i)
    z+=1
