import pandas as pd
df = pd.DataFrame({'Last': ['Gaitonde', 'Singh', 'Mathur'],
                   'First': ['Ganesh', 'Sartaj', 'Manish']})
print("before join")
print(df,"\n")
print("after join")
df['Name']=df['First'].str.cat(df['Last'],sep=" ")
print(df)

df['Name2']=df[['First','Last']].apply(lambda x: ' '.join(x),axis=1)
print(df)

df['Name3']=df["First"].astype(str)+" "+df["Last"]
print(df)
