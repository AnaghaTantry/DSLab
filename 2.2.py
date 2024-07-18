import numpy as np
#Input the matrix
matrix = np.array([[1, 2], [4, 5]])
#Calculate the eigenvalues of the matrix
eigenvalue = np.linalg.eigvals(matrix)
#Print the results
print("Matrix: ")
print(matrix)
print("Eigenvalues: ")
print(eigenvalue)