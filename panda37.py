import pandas as pd
sr=pd.Series(['New York', 'Chicago', 'Toronto', 'Lisbon', 'Rio', 'Chicago', 'Lisbon'])
print(sr)
print(sr.value_counts())
sr = pd.Series([100, 214, 325, 88, None, 325, None, 325, 100])
print(sr)
print(sr.value_counts())
