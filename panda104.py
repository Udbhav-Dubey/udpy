import pandas as pd
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Nagpur', 'Kanpur', 'Allahabad', 'Kannuaj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
df=pd.DataFrame(data)
new=df["Age"].copy()
df["Name"]=df["Name"].str.cat(df["Address"],sep=", ")
print(df)
