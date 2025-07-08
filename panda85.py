import pandas as pd
import numpy as np
df1 = pd.DataFrame(
    {
        "Stationary": ["Pens", "Scales",
                       "Pencils", "Geometry Box",
                       "Crayon Set"],
        "Price": [100, 50, 25, 100, 65],
        "Quantity": [10, 5, 5, 2, 1]
    },
    columns=["Stationary", "Price", "Quantity"],
)
print(df1)
df2 =df1.copy()
df2.loc[0, 'Price'] = 100 
df2.loc[1, 'Price'] = 70
df2.loc[2, 'Price'] = 30
df2.loc[0, 'Quantity'] = 15
df2.loc[1, 'Quantity'] = 7
df2.loc[2, 'Quantity'] = 6

print(df2)
print(df1.compare(df2))
print(df1.compare(df2,align_axis=0))
print(df1.compare(df2,align_axis=0,keep_equal=False))
print(df1.compare(df2,align_axis=0,keep_equal=True))
print(df1.compare(df2,align_axis=0,keep_shape=True,keep_equal=True))
