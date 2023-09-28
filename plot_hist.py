#The below file takes a csv file called 'data.csv' file.
#I created a dataframe from it and built a histogram using the data.
#Here's the code

import matplotlib

import pandas as pd
import matplotlib.pyplot as plt

f=pd.read_csv('data.csv')
f["Duration"].plot(kind='hist')
plt.title('Histogram') #Creates a title for the plot
plt.show() 
