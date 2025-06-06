def f():
    a="i am local around these parts"
    print(a)

f()

b="baine is global"

def fb():
    global b
    b="batman is now global baine dead"
    print(b)

fb()
print(b)
