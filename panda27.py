import pandas as pd
 
# dictionary of lists
dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["BCA", "BCA", "M.Tech", "BCA"],
        'score':[90, 40, 80, 98]}
 

df = pd.DataFrame(dict, index = [0, 1, 2, 3])

mask = df.index <=1 

print(df[mask])
