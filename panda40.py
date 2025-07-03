import pandas as pd
values= [['A',455],['B',250],['C',495],
         ['D',400],['E',350],['F',450]]
df=pd.DataFrame(values,columns=['Name','Total Marks'])
print(df)
df=df.assign(percentage=lambda x:(x['Total Marks']/500*100))
print(df)
