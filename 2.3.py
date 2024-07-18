import numpy as np
#Create matrices and vectors
matrix_A = np.array([[1, 2], [3, 4]])
matrix_B = np.array([[5, 6], [7, 8]])
vector_x = np.array([1, 2])
vector_y = np.array([3, 4])
#Dot product of two vectors
dot_product = np.dot(vector_x, vector_y)
#Inner product of two matrices
inner_product = np.inner(matrix_A, matrix_B)
#Outer product of two vectors
outer_product = np.outer(vector_x, vector_y)
#Matrix product of two matrices
matrix_product = np.matmul(matrix_A, matrix_B)
#Matrix exponentiation
exponent = 2
matrix_exponentiation = np.linalg.matrix_power(matrix_A, exponent)
#Print the results
print("Matrix A: ")
print(matrix_A)
print("Matrix B: ")
print(matrix_B)
print("Vector x: ")
print(vector_x)
print("Vector y: ")
print(vector_y)
print("Dot product of two Vectors: ")
print(dot_product)
print("Inner product of two Matrices: ")
print(inner_product)
print("Outer product of two Vectors: ")
print(outer_product)
print("Matrix product of two Matrices: ")
print(matrix_product)
print(f"Matrix A raised to the power {exponent}: ")
print(matrix_exponentiation)




