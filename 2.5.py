import pandas as pd
#Create a pandas Series with labels
data = {'A':10, 'B':20,'C':30, 'D':40}
series = pd.Series(data)
#Print the series
print("Panda Series: ")
print(series)
#Accessing the elements by label
print("\nAccessing the elements by label: ")
print("Value at label 'A': ",series['A'])
print("Value at label 'B': ",series['B'])
#Accessing the elements by position
print("\nAccessing the elements by position: ")
print("3rd element: ",series.iloc[2])
print("4th element: ",series.iloc[3])
#Arithmetic operation on the series
print("\nArithmetic operations of the series: ")
result = series*2
print("Series multiplied by 2: ",result)
#Filtering elements
print("\nFiltering elements: ")
filtered_series = series[series>20]
print("Elements greater than 20: ")
print(filtered_series)