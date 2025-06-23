keys = ['a','b','c','d','e']
values = [1,2,3,4,5]  
myDict = { k:v for (k,v) in zip(keys, values)}  
print (myDict)

dic2=dict.fromkeys(range(5),True)
print(dic2)

dict={x:x**2 for x in [1,2,3,4,5]}
print(dict)

newdict={x:x**3 for x in range(10) if x**3 % 4==0}
print(newdict)
