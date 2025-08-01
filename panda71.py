import pandas as pd

data1 = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'],
        'Age':[27, 24, 22, 32],
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}

data2 = {'Name':['Abhi', 'Ayushi', 'Dhiraj', 'Hitesh'],
        'Age':[17, 14, 12, 52],
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'],
        'Qualification':['Btech', 'B.A', 'Bcom', 'B.hons']}

df1 = pd.DataFrame(data1,index=[0, 1, 2, 3])

df2 = pd.DataFrame(data2, index=[4, 5, 6, 7])

print(df1, "\n\n", df2)
res=pd.concat([df1,df2],keys=['x','y'])
print(res)
s1 = pd.Series([1000, 2000, 3000, 4000], name='Salary')
print(df1,"\n\n",s1)
res1=pd.concat([df1,s1],axis=1)
print(res1)
