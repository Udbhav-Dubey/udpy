import pandas as pd
dict={'name':["ud","bh","av","du"],
      'degree':["be","10th","12th","bt"],
      'score':[90,50,30,20]}
df=pd.DataFrame(dict)
print(df)
for key,value in df.iterrows():
    print(key,value)
    print()
