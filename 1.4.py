import numpy as np
#Create a sample NumPy array
arr = np.array([ [1, 2, 3], [4, 5, 6], [7, 8, 9] ])
#Get the number of dimensions of the array (ndim)
num_dimensions = arr.ndim
#Get the shape of the array
array_shape = arr.shape
#Get the size of the array
array_size = arr.size
#Get the data type of the array
data_type = arr.dtype
#Print the results
print("Original Array: ")
print(arr)
print("Number of Dimensions: ",num_dimensions)
print("Shape of the Array: ",array_shape)
print("Size of the Array: ",array_size)
print("Data Type: ",data_type)