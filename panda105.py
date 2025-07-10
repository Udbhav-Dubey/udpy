import pandas as pd
data = {'Name':['Jai', 'Princi', 'Gaurav', 'Anuj'], 
        'Age':[27, 24, 22, 32], 
        'Address':['  Nagpur junction    ', '  Kanpur junction  ', 
                   'Nagpur junction       ', '  Kannuaj junction   '], 
        'Qualification':['Msc', 'MA', 'MCA', 'Phd']}
df=pd.DataFrame(data)
print(df)
df["Address"]=df["Address"].str.strip()
print(df)
