import pandas as pd
df1 = pd.DataFrame({'Data': [11, 12, 13, 14]})
df2 = pd.DataFrame({'Data': [21, 22, 23, 24]})
df3 = pd.DataFrame({'Data': [31, 32, 33, 34]})
writer=pd.ExcelWriter('Pandas multi sheet.xlsx',engine='xlsxwriter')
df1.to_excel(writer,sheet_name='1')
df2.to_excel(writer,sheet_name='2')
df3.to_excel(writer,sheet_name='3')
writer.close()
