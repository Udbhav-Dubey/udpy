import pandas as pd
import numpy as np
idx=pd.Index(['Python','Java','php'])
print(idx.value_counts())
a=pd.Index(['py','java','py'])
print(a.value_counts())
print(a.value_counts(normalize=True))
print(a.value_counts(sort=True))
print(a.value_counts(ascending=True))
