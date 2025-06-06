def cube(y):
    print(f"finding cube of number :{y}")
    return y * y * y 

lambda_cube = lambda num: num**3

print("involving function defined with def keyword: ")
print(cube(30))

print("invoking lambda function : ",lambda_cube(30))
