import pandas as pd
dataframe = pd.DataFrame(
    {'Marks (Out of 50)': [30, 40, 45, 15, 8, 5, 35],
     'Percentage': [.6,   .8,   .9,  .3,  .16,   .1,  .7 ], })
 
writer_object = pd.ExcelWriter("Example_column.xlsx",
                                engine ='xlsxwriter')
 
dataframe.to_excel(writer_object, sheet_name ='Sheet1')
 
workbook_object = writer_object.book
 
worksheet_object = writer_object.sheets['Sheet1']
 
 
format_object1 = workbook_object.add_format({'num_format': '# 0.00'})
 
format_object2 = workbook_object.add_format({'num_format': '0 %'})
worksheet_object.set_column('B:B', 20, format_object1)
 
worksheet_object.set_column('C:C', 15, format_object2)
 
writer_object.close()
