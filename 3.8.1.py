import pandas as pd
#Load the dataset from a CSV file
titanic_data = pd.read_csv('EDA_Excel.csv')
#Display the first 2 rows of the DataSet
print("First two rows of the Dataset: ")
print(titanic_data.head(2))
#Get basic Statistics of the Dataset
summary_stats = titanic_data.describe()
print("\nSummary Statistics: ")
print(summary_stats)
#Filter the passengers who survived (Survived = 1)
survived_passengers = titanic_data[titanic_data['Survived']==1]
print("\nPassengers who survived: ")
print(survived_passengers.head())
#Filter the passengers in First Class (Pclass = 1)
firstclass_passengers = titanic_data[titanic_data['Pclass']==1]
print("\nPassengers in First Class: ")
print(firstclass_passengers.head())
#Group the passengers by class and calculate the mean age for each class
mean_age_by_class = titanic_data.groupby('Pclass')['Age'].mean()
print("\nMean Age by Class: ")
print(mean_age_by_class)
#Sort the dataset by age in descending order
sorted_by_age = titanic_data.sort_values(by = 'Age', ascending = False)
print("\nPassengers sorted by descending values: ")
print(sorted_by_age.head())
#Count the number of passengers in each class
passenger_count_by_class = titanic_data['Pclass'].value_counts()
print("\nPassenger Count by Class: ")
print(passenger_count_by_class)
#Calculate the correlation between 'Fare' and 'Age' columns
correlation = titanic_data['Fare'].corr(titanic_data['Age'])
print("\nCorrelation between Fare and Age: ", correlation)