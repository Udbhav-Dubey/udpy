def tail_fact(n,acc=1):
    if n==0:
        return acc
    else :
        return tail_fact(n-1,acc*n)
def nontail_fact(n):
    if n==1:
        return 1
    else :
        return n * nontail_fact(n-1)

print(tail_fact(5))
print(nontail_fact(5))
