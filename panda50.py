import pandas as pd
sr = pd.Series([19.5, 16.8, 22.78, 20.124, 18.1002])
print(sr)
result=sr.truncate(before = 1, after = 3)
print(result)
