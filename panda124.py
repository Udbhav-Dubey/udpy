import pandas as pd
import matplotlib.pyplot as plt
df = pd.DataFrame({
    'x': [1, 2, 3, 4],
    'y': [10, 20, 30, 40]
})

ax = df.plot()
print(type(ax))
plt.show()
