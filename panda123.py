import pandas as pd
import numpy as np
df1=pd.read_csv("df1.csv",index_col=0)
df2=pd.read_csv("df2.csv")
print(df2.plot())
