#8: Check if a String is Palindrome using Recursion
def func(s,i,j):
    if (i>=j):
        return True
    if (s[i]!=s[j]):
        return False
    if (s[i]==s[j]):
        return func(s,i+1,j-1)
    
s=input("enter the string : ")
res=func(s,0,len(s)-1)
print(res)
