import numpy as np
records=[(1,'alice',25.5),(2,'bob',3.33),(3,'ok',44.3)]
dtyped=[('id','i4'),('name','U10'),('age','f4')]
structured_array=np.rec.fromrecords(records,dtype=dtyped)
print(structured_array)
print(structured_array["name"])
print(structured_array["age"])
