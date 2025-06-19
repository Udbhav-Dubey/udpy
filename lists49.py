a=[4,5,7,52,6,65,7,645]
indices=[]
start=0
while True:
    try :
        index=a.index(7,start)
        indices.append(index)
        start=index+1
    except ValueError:
        break
print("indices",indices)
