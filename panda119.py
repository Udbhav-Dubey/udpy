import pandas as pd
from datetime import datetime, date
dataframe = pd.DataFrame({
    'Date and time': [ datetime(2018, 1, 11, 11, 30, 55),
                      datetime(2018, 2, 12, 1,  20, 33),
                      datetime(2018, 3, 13, 11, 10    ),
                      datetime(2018, 4, 14, 16, 45, 35),
                      datetime(2018, 5, 15, 12, 10, 15)],

   'Dates only':    [ date(2018, 6, 21),
                      date(2018, 7, 22),
                      date(2018, 8, 23),
                      date(2018, 9, 24),
                      date(2018, 10, 25) ], })
writer_object = pd.ExcelWriter("Example_datetime.xlsx",
                        engine ='xlsxwriter',
                        datetime_format ='mmm d yyyy hh:mm:ss',
                        date_format ='mmmm dd yyyy')
 
dataframe.to_excel(writer_object, sheet_name ='Sheet1')
 
worksheet_object  = writer_object.sheets['Sheet1']
 
worksheet_object.set_column('B:C', 20)
 
writer_object.close()
