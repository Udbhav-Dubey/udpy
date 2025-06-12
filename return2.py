def fun1(msg):
    def fun2():
        return f"Message : {msg}"
    return fun2

fun3=fun1("hello,world!")

print(fun3())
