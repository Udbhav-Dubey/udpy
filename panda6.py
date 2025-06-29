import pandas as pd
ser1= pd.Series([1,2,3],index=['A','B','c'])
ser2= pd.Series([4,5,6],index=['A','B','C'])
df_sum=ser1.add(ser2)
print(df_sum)

ser=pd.Series([1,2,3,4])
ser=ser.astype(float)
print(ser)
