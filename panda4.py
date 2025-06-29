import pandas as pd
data=[1,2,3,4,5,6,7,8,9,10,11,12,13]
ser=pd.Series(data)
print(ser)
print("element at index 3 : ",ser[3])
print(ser[:7:2])
str="udbhav dubey"
strl=list(str)
ser=pd.Series(strl,index=[10,11,12,13,14,15,16,17,18,19,20,21])
print(ser[15])

