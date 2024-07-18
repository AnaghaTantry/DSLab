import numpy as np
#Define the coefficient matrix(A) and the right hand side vector(b) 
A = np.array([[1,2], [3,4]])
b = np.array([1,2])
#Solve the system of linear equations
solution = np.linalg.solve(A, b)
#Print the results
print("Coefficient Matrix(A): ")
print(A)
print("Right Hand Side Vector(b): ")
print(b)
print("Solution Vector(x): ")
print(solution)

