import pandas as pd
data = {
    'Category' : ['A', 'B', 'A', 'B', 'C'],
    'Values' : [10, 18, 10, 12, 8]
}
df = pd.DataFrame(data)
#Group the DataFrame by 'Category' column
grouped = df.groupby('Category')
#Calculate the sum of 'Values' for each group
sum_by_category = grouped['Values'].sum()
print("Sum of Values for each Category: ")
print(sum_by_category)
#Calculate the mean of 'Values' for each group
mean_by_category = grouped['Values'].mean()
print("Mean of Values for each Category: ")
print(mean_by_category)
#Multiple grouping
grouped_multiple = df.groupby(['Category', 'Values'])
#Count the number of occurances for each combination of 'Category' and 'Values'
count_by_category_values = grouped_multiple.size()
print("Count by Category and Values: ")
print(count_by_category_values)
