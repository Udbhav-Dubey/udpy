tple=("geeks","for","geeks")
l_element=len(tple)-1
tple=tple[:l_element]
print(tple)

tple=("geeks","for","geeks")
tple=tple[:-1]
print(tple)

tple=("geeks","for","geeks")
temp=list(tple)
temp.pop(-1)
tple=tuple(temp)
print(tple)

temp=list(tple)
temp.remove(temp[-1])
tple=tuple(temp)
print(tple)

tu = (1, 2, 3, 4, 5)
tu = tuple(filter(lambda x: x != tu[-1], tu))
print(tu)
