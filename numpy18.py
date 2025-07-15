import numpy as np
org_array=np.array([1.554, 2.99, 3.42, 4.87, 6.94,
                      8.21, 7.65, 10.50, 77.5])
print(org_array)
copy_array=np.copy(org_array)
print("copy array : ",copy_array)
d2_array=np.array([[23, 46, 85],
                      [43, 56, 99],
                      [11, 34, 55]])
print(d2_array)
d2copy=np.copy(d2_array)
print("copied array\n",d2copy)

org_array = np.array([[99, 22, 33],
                      [44, 77, 66]])
copyy=org_array
org_array[1,2]=13.33
print("orginal :",org_array)
print("copied  :",copyy)
