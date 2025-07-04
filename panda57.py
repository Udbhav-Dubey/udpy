import pandas as pd
dict={'name':["ud","bh","av","du"],
      'degree':["be","10th","12th","bt"],
      'score':[90,50,30,20]}
data=pd.DataFrame(dict)
print(data)
for i in data.itertuples():
    print(i)
