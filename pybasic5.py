#Exercise 6: Display numbers divisible by 5 Write a Python code to display numbers from a list divisible by 5
l1=list(map(int,input().split()))
for i in l1:
    if i%5==0:   
            print(i)

