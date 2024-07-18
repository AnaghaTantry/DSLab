import numpy as np
#Create a sample NumPy array
arr = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
#Slicing
slice_result = arr[2:7]
print("Slicing result: ",slice_result)
#Array indexing result
index_result = arr[[1,3,5]]
print("Array indexing result: ",index_result)
#Boolean indexing result
boolean_condition = arr % 2 == 0
boolean_indexing_result = arr[boolean_condition]
print("Boolean indexing result: ",boolean_indexing_result)
