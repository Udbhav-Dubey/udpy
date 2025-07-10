import pandas as pd
sr=pd.Series([10,25,3,11,24,6])
index_ = ['Coca Cola', 'Sprite', 'Coke', 'Fanta', 'Dew', 'ThumbsUp']
sr.index=index_
print(sr)
result=sr.replace(to_replace=[3,10],value=[1000,3000])
print(result)

