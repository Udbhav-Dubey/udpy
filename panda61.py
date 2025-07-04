import pandas as pd
data = {"Name": ["Alice", "Bob"], "Age": [25, 30],"height":[6,5.5]}
df=pd.DataFrame(data)
df.loc[len(df)]=["Charlie",35,5.7]
print(df)
df.loc[len(df)]=["unknown",0,0]
print(df)
new_row=pd.DataFrame({"Name":["Eve"],"Age":[28],"weight":55})
df=pd.concat([df,new_row],ignore_index=True)
print(df)
new_rows = pd.DataFrame({"Name": ["Charlie", "Diana"], "Age": [35, 28]})
df = pd.concat([df, new_rows], ignore_index=True)
print(df)
