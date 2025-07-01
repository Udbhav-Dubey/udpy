import pandas as pd
 
dict = {'name':["aparna", "pankaj", "sudhir", "Geeku"],
        'degree': ["MBA", "BCA", "M.Tech", "MBA"],
        'score':[90, 40, 80, 98]}
 
df = pd.DataFrame(dict, index = [0, 1, 2, 3])
 


print(df[[True, False, True, False]])#sirf true vale hi show honge 
