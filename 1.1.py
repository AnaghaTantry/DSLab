import numpy as np
#Create a NumPy array from a list with float type
my_list = [1.9, 2.1, 3.2, 4.3, 5.4]
array_from_list = np.array(my_list, dtype = float)
#Create a NumPy array from a tuple with float type
my_tuple = (1.9, 2.1, 3.2, 4.3, 5.4)
array_from_tuple = np.array(my_tuple, dtype = float)
#Print the results
print("Array from List: ",array_from_list)
print("Array from Tuple: ",array_from_tuple)
