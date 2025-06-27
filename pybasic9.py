#Exercise 10: Merge two lists using the following condition Given two lists of numbers, write Python code to create a new list containing odd numbers from the first list and even numbers from the second list.
list1=list(map(int,input().split()))
list2=list(map(int,input().split()))
list3=[]
len=max(len(list1),len(list2))
for i in range(len):
    if i < len(list1): 
        if list1[i]%2!=0 : 
            list3.append(list1[i])
    if i < len(list2):
        if list2[i]%2==0:
            list3.append(list2[i])
print(list3)
