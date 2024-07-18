import pandas as pd
#Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age' : [23, 30, 25, 18],
    'Place': ['New York', 'San Fransisco', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
#Column Selection
selected_columns = df[['Name', 'Age']]
print("Selected Columns: ")
print(selected_columns)
#Column Addition
df['Salary'] = [20000, 40000, 30000, 15000]
print("\nDataFrame after adding Salary column: ")
print(df)
#Column deletion
df.drop('Place', axis = 1, inplace = True)
print("\nDataFrame after deleting 'Place' column: ")
print(df)