import numpy as np
import pandas as pd
#Create a sample DataFrame
data = {
    'A': [1, 2, 3, 4],
    'B': [5, 6, 7, 8]
}
df =pd.DataFrame(data)
#Convert DataFrames to Numpy array using .values attribute
numpy_array_df = df.values
#Create a sample Series
series = pd.Series([10, 20, 30, 40])
#Convert Series to Numpy array using .values attribute
numpy_array_series = series.values
#Convert DataFrames to Numpy array using to_numpy() attribute
numpy_array_df_alt = df.to_numpy()
#Convert Series to Numpy array using to_numpy() attribute
numpy_array_series_alt = series.to_numpy()
#Print the results
print("DataFrame to NumPy Array (Using .values attribute): ")
print(numpy_array_df)
print("Series to NumPy Array (Using .values attribute): ")
print(numpy_array_series)
print("DataFrame to NumPy Array (Using to_numpy() method): ")
print(numpy_array_df_alt)
print("Series to NumPy Array (Using to_numpy() method): ")
print(numpy_array_series_alt)







