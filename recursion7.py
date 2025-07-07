#Problem #7: Reverse an array using recursion (without extra space

def reverse(li,i,j):
    if i >=j:
        return
    li[i],li[j]=li[j],li[i]
    reverse(li,i+1,j-1)

li=list(map(int,input("please enter the numbers with space: ").split()))
reverse(li,0,len(li)-1)
print(li)
