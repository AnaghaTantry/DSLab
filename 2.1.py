import numpy as np
#Input the matrix
matrix = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
#Calculate the rank of the matrix
rank = np.linalg.matrix_rank(matrix)
#Calculate the determinant of the matrix
determinant = np.linalg.det(matrix)
#Calculate the trace of the matrix
trace = np.trace(matrix)
#Print the results
print("Matrix: ")
print(matrix)
print(f"Rank of the Matrix: {rank}")
print(f"Determinant of the Matrix: {determinant}")
print(f"Trace of the Matrix: {trace}")