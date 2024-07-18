import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
#Load the Titanic dataset from a CSV file
titanic_data = pd.read_csv('EDA_excel.csv')
#Display the first 5 rows of the Dataset
print("First 5 rows of the Dataset: ")
print(titanic_data.head())
#Get Basic statistics of the dataset
summary_stats = titanic_data.describe()
print("\nSummary Statistics: ")
print(summary_stats)
#Plot a histogram by passengers' ages
plt.figure(figsize = (8, 6))
sns.histplot(titanic_data['Age'], bins = 20, kde = True)
plt.title("Age Distribution of Passengers: ")
plt.xlabel("Age")
plt.ylabel("Frequency")
plt.show()
#Plot a bar chart for passengers class counts
plt.figure(figsize = (8,6))
sns.countplot(data = titanic_data, x = 'Pclass')
plt.title("Passenger Class Counts: ")
plt.xlabel("Class")
plt.ylabel("Counts")
plt.show()
#Create a heatmap to visualise the correlation between numerical columns
numeric_columns = titanic_data.select_dtypes(include = [np.number])
correlation_matrix = numeric_columns.corr()
plt.figure(figsize = (8,6))
sns.heatmap(correlation_matrix, annot = True, cmap = 'coolwarm')
plt.title("Correlation HeatMap")
plt.show()
