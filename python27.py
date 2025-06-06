a=10
b=12
def add() : 
    c=a+b
    print(c)

add()
def fun():
    var=10
    
    def gun():
        nonlocal var 
        var+=10
        print(var)

    gun()

fun()
