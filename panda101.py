import pandas as pd 
dRan1 = pd.date_range(start ='1-1-2018', periods = 13) 
dRan2 = pd.date_range(end ='1-1-2018', periods = 13) 
dRan3 = pd.date_range(start ='01-03-2017',  
            end ='1-1-2018', periods = 13) 
print(dRan1, "\n\n", dRan2, '\n\n', dRan3)
dRan1 = pd.date_range(start='1-1-2018', periods=13, tz='Asia/Tokyo')
print(dRan1)
