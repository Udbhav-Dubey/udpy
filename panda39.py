import pandas as pd
import numpy as np
a = pd.Index(['apple', np.nan, 'banana', np.nan])
print(a.value_counts(dropna=False))

b = pd.Index([5, 15, 25, 10])
print(b.value_counts(bins=2))
