list1=list(map(int,input().split()))
list2=list(map(int,input().split()))
list3=[]
odd=[x for x in list1 if x % 2 !=0]
even=[x for x in list2 if x %2 ==0]
result=odd + even
print(result)
