import pandas as pd
data1 = ["Math", "Physics", "Computer",
         "Hindi", "English", "chemistry"]
data2 = [95, 78, 80, 80, 60, 95]
data3 = [90, 67, 78, 70, 63, 90]
dataframe = pd.DataFrame(
    {'Subject': data1,
     'Mid Term Exam Scores Out of 100' : data2,
     'End Term Exam Scores Out of 100' : data3})
 
writer_object = pd.ExcelWriter("Example_header.xlsx",
                                engine ='xlsxwriter')
 
dataframe.to_excel(writer_object, sheet_name ='Sheet1', 
                          startrow = 1, header = False)
 
workbook_object = writer_object.book
 
worksheet_object = writer_object.sheets['Sheet1']
 
header_format_object = workbook_object.add_format({
                                'bold': True,
                                'italic' : True,
                                'text_wrap': True,
                                'valign': 'top',
                                'font_color': 'red',
                                'border': 2})
 
for col_number, value in enumerate(dataframe.columns.values):
    worksheet_object.write(0, col_number + 1, value, 
                              header_format_object)
writer_object.close()
