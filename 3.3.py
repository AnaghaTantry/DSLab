import pandas as pd
#Create a sample DataFrame
data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David'],
    'Age' : [23, 30, 25, 18],
    'Place': ['New York', 'San Fransisco', 'Los Angeles', 'Chicago']
}
df = pd.DataFrame(data)
#Row selection
selected_row = df.loc[1]
print("Selected Row: ")
print(selected_row)
#Row addition
new_row = pd.Series(['Eva', 28, 'Miami'], index = ['Name', 'Age', 'Place'])
df=pd.concat([df,pd.DataFrame([new_row])],ignore_index=True)
print("DataFrame after adding new row:: ")
print(df)
#Row deletion
df.drop(2, inplace = True)
print("DataFrame after deleting third row: ")
print(df)