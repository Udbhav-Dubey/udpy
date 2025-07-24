A = [[1,2],[4,5]] 
B = [[7,8],[9,10]] 
rows = len(A) 
cols = len(A[0]) 

# Element wise addition 
C = [[0 for i in range(cols)] for j in range(rows)] 
for i in range(rows): 
	for j in range(cols): 
		C[i][j] = A[i][j] + B[i][j] 
print("Addition of matrices: \n", C) 

# Element wise subtraction 
D = [[0 for i in range(cols)] for j in range(rows)] 
for i in range(rows): 
	for j in range(cols): 
		D[i][j] = A[i][j] - B[i][j] 
print("Subtraction of matrices: \n", D) 

# Element wise division 
E = [[0 for i in range(cols)] for j in range(rows)] 
for i in range(rows): 
	for j in range(cols): 
		E[i][j] = A[i][j] / B[i][j] 
print("Division of matrices: \n", E)
