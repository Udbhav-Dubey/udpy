import pandas as pd
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['Delhi', 'Kanpur', 'Allahabad', 'Kannauj'], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']} 

df=pd.DataFrame(data)
df["Name"]=df["Name"].str.lower()
print(df)
df["Name"]=df["Name"].str.upper()
print(df)
df.dropna(inplace=True)
df["Address"]=df["Address"].str.split("a",n=1)
df["Address"]=df["Address"].str.join("v")
print(df)
