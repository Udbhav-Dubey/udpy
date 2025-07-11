import pandas as pd
df=pd.DataFrame({'Data':["y2j","hbk","rock","hhh","goku","vegeta","cena"]})
writer=pd.ExcelWriter('pandaEx.xlsx',engine='xlsxwriter')
df.to_excel(writer,sheet_name="sheet1")
writer.close()

