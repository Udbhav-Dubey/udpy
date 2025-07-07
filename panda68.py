import pandas as pd
data = {
    'Store': ['A', 'A', 'B', 'B', 'A', 'B'],
    'Product': ['Apple', 'Banana', 'Apple', 'Banana', 'Apple', 'Banana'],
    'Sales': [100, 150, 200, 100, 120, 180],
    'Quantity': [10, 20, 30, 40, 15, 35]
}
df=pd.DataFrame(data)
print(df)
agg_dict={
    'Sales' : ['sum','mean'],
    'Quantity': ['max','min']
}
result=df.groupby('Store').agg(agg_dict).reset_index()
print("\n",result)
agg_dict2={
    'Sales': lambda x : x.max() - x.mean(),
    'Quantity':'sum'
}
result2=df.groupby('Product').agg(agg_dict2).reset_index()
print("\n",result2)
