import pandas as pd
df = pd.DataFrame({
    'Math': [90, 85, 80],
    'Physics': [70, 75, 78]
}, index=['Alice', 'Bob', 'Charlie'])
df.plot()

