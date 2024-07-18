import pandas as pd
#Create a pandas DataFrame
data = {
    'Name' : ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age' : [25, 30 ,22, 18, 23],
    'Place' : ['New York', 'San Fransisco', 'Los Angeles', 'Chicago', 'Miami']
}
df = pd.DataFrame(data)
#Use describe() to get summary statistics
print("DataFrame Statistics: ")
print(df.describe())
#Use head() to display first few rows (default is 5)
print("\nFirst 3 rows: ")
print(df.head(3))
#Use tail() to display last few rows (default is 5)
print("\nLast 2 rows: ")
print(df.tail(2))
