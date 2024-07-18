import pandas as pd
#Create a dictionary of data
data =  {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age': [25, 30, 22, 18],
    'City': ['New York', 'Los Angeles', 'San Fransisco', 'Chicago']
}
#Create a Pandas DataFrame
df = pd.DataFrame(data)
#Print the DataFrame
print(df)