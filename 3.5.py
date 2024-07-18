import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
#Create a sample DataFrame
data = {
    'Category' : ['A', 'B', 'C', 'D'],
    'Values' : [10, 20, 32, 18]
}
df = pd.DataFrame(data)
#Bar plots
df.plot(x = 'Category', y ='Values', kind = 'bar', title = 'Bar Plot')
plt.show()
#Histogram
data = {
    'Values' : np.random.normal(0, 1, 1000)
}
df = pd.DataFrame(data)
df['Values'].plot(kind='hist', title='Histogram', edgecolor='black', bins = 20)
plt.show()
#Line plots
data = {
    'X' : np.arange(0, 10, 0.1),
    'Y' : np.sin(np.arange(0, 10, 0.1))
}
df = pd.DataFrame(data)
df.plot(x = 'X', y = 'Y', kind = 'line', title = 'Line Plot')
plt.show()
#Scatter plots
data = {
    'X' : np.random.rand(50),
    'Y' : np.random.rand(50)
}
df = pd.DataFrame(data)
df.plot(x= 'X', y = 'Y', kind = 'scatter', title = 'Scatter plot', c ='b' )
plt.show()