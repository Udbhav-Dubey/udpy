import numpy 
print("numpy random is a ",type(numpy))
print("it contains :",dir(numpy)[-15:])
roll=numpy.random.randint(low=1,high=6,size=10)
print(roll)
print(type(roll))
print(roll.mean())
rollli=roll.tolist()
print(rollli)
arr=[1,2,3,4,5,6]
#arr10=[1,2,3,4,5,6]+10
arrr=numpy.array(arr)
arr10=arrr+10
print(arr10)
print(roll<=3)
print(arrr[-1])
