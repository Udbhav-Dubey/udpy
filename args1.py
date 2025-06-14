def fun (*args):
    return sum(args)
print(fun(1,2,4,5))

def fun_k(**kwargs):
    for k ,val in kwargs.items():
        print(k,val)
fun_k(a=1,b=2,c=3)
