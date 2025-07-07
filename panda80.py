import pandas as pd
first =[1, 2, 5, 6, 3, 7, 11, 0, 4]
second =[5, 3, 2, 1, 3, 9, 21, 3, 1]
s1=pd.Series(first,index=['a','b','c','d','e','f','g','h','i'])
s2=pd.Series(second,index=['a','b','c','d','e','f','g','h','i'])
result=s1.combine(s2,(lambda x1,x2 : x1 if x1 < x2 else x2))
print(result)
