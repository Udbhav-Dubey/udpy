import pandas as pd

example = {'Team':['Australia', 'England', 'South Africa',
                   'Australia', 'England', 'India', 'India',
                        'South Africa', 'England', 'India'],
                        
           'Player':['Ricky Ponting', 'Joe Root', 'Hashim Amla',
                     'David Warner', 'Jos Buttler', 'Virat Kohli',
                     'Rohit Sharma', 'David Miller', 'Eoin Morgan',
                                                 'Dinesh Karthik'],
                                                 
          'Runs':[345, 336, 689, 490, 989, 672, 560, 455, 342, 376],
          
          'Salary':[34500, 33600, 68900, 49000, 98899,
                    67562, 56760, 45675, 34542, 31176] }

df = pd.DataFrame(example)

total_salary = df['Salary'].groupby(df['Team'])
print(total_salary.mean())
