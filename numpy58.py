import numpy as np
print("is real : ",np.isreal([1+1j,0j]),"\n")
print("is real : ",np.isreal([1,0]),"\n")
complex1=2+4j;
print("conjugate of ",complex1,"is",np.conj(complex1))

arr1 = [1, 27000, 64, -1000]
print ("cbrt Value of arr1 : \n", np.cbrt(arr1))
  
arr2 = [1024 ,-128]
print ("\ncbrt Value of arr2 : ", np.cbrt(arr2))
 
in_array = [1, 2, 3, 4, 5, 6, 7, 8 ]
print ("Input array : ", in_array)
 
out_array = np.clip(in_array, a_min = 2, a_max = 6)
print ("Output array : ", out_array)
