import pandas as pd
dict={'name':["ud","bh","av","du"],
      'degree':["be","10th","12th","bt"],
      'score':[90,50,30,20]}
df=pd.DataFrame(dict)
columns=list(df)
for i in columns:
        print(df[i][2])
