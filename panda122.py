import pandas as pd
dataframe = pd.DataFrame({
                    'Subject': ["Math", "Physics", "Computer",
                                "Hindi", "English", "chemistry"],
                   'Mid Exam Score' :  [90, 78, 60, 80, 60, 90],
                   'End Exam Score' : [45, 39, 30, 40, 30, 60] })
writer_object=pd.ExcelWriter('Pandas_column_chart.xlsx',engine='xlsxwriter')
dataframe.to_excel(writer_object,sheet_name="sheet1")
workbook_object=writer_object.book
worksheet_object=writer_object.sheets['sheet1']
worksheet_object.set_column('B:C',20)
chart_object=workbook_object.add_chart({'type':'column'})
chart_object.add_series({
                        'name':['sheet1',0,2],
                        'categories':['sheet1',0,3,6,3],
                        'values':['sheet1',1,2,6,2],
})
chart_object.set_title({'name':'exam score distibution'})
chart_object.set_x_axis({'name':'subject'})
chart_object.set_y_axis({'name':'marks'})
worksheet_object.insert_chart('E2',chart_object,{'x_offset':20,'y_offset':5})
writer_object.close()
