# Project 2018 - Programming and Scripting
# Guilherme G. C. Paes - 2018

# After some research I've found out that for the purpose of this project numpy, pandas, seaborn and matplotlib would be the best libraries to use
# Importing the libraries:
import numpy as np
import pandas as pd
import matplotlib.pyplot as pl
import seaborn as sns

# Importing the dataset from iris.csv file
iris = pd.read_csv("iris.csv", names = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Class"])


#DATASET ANALYSIS
#Printing some data just for visualization
print(iris.sample(10))
print()

# Printing the rows and columns of the data using the shape property:
print("The iris dataset has", iris.shape, "rows and columns respectively")
print()

# Class Distribution
print(iris.groupby('Class').size())
print()

#Calculating the mean of each column using numpy
print("This is the mean value for each column: \n", np.mean(iris))
print()

#Calculating the max of each column using numpy
print("This is the maximum value for each column: \n",np.max(iris))
print()

#Calculating the min of each column using numpy
print("This is the minimum value for each column: \n",np.min(iris))
print()

#For better visualization, the pandas library shows a better summary of the data, such as mean, max, min, std
print(iris.describe())
print()

#Used pands pivot table to generate the Min, Mean and Max for each class

print("Min for each class: \n", pd.pivot_table(iris, index=['Class'], aggfunc='min'))
print()
print("Mean for each class: \n", pd.pivot_table(iris, index=['Class'], aggfunc='mean'))
print()
print("Max for each class: \n", pd.pivot_table(iris, index=['Class'], aggfunc='max'))
print()
print("Std for each class: \n", pd.pivot_table(iris, index=['Class'], aggfunc='std'))
print()



#CHARTS
#First generating single histogram for each class using matplotlib

#Creating a Histogram only of Sepal Lenght
iris.hist('Sepal Length') 
pl.title('Histogram of Sepal Lenght') 
pl.xlabel('Sepal Lenght in cm') 
pl.ylabel('Sample Number')  
pl.savefig('iris_histogram_sepallenght.png')  
pl.show() 

#Creating a Histogram only of Sepal Width
iris.hist('Sepal Width') 
pl.title('Histogram of Sepal Width') 
pl.xlabel('Sepal Width in cm') 
pl.ylabel('Sample Number')  
pl.savefig('iris_histogram_sepalwidth.png')  
pl.show() 

#Creating a Histogram only of Petal Lenght
iris.hist('Petal Length') 
pl.title('Histogram of Petal Lenght') 
pl.xlabel('Petal Lenght in cm') 
pl.ylabel('Sample Number')  
pl.savefig('iris_histogram_petallenght.png')  
pl.show() 

#Creating a Histogram only of Petal Width
iris.hist('Petal Width') 
pl.title('Histogram of Petal Width') 
pl.xlabel('Petal Width in cm') 
pl.ylabel('Sample Number')  
pl.savefig('iris_histogram_petalwidth.png')  
pl.show() 


# Creating a single Histogram for all Classes
iris.hist()
pl.savefig('iris_histogram.png') 
pl.show()

# Generating Box and Whisker plot
iris.plot(kind='box', sharex=False, sharey=False)
pl.title('Box and Whisker Plot') 
pl.ylabel('cm')  
pl.savefig('iris_box_and_whisker_plot.png')
pl.show()

# Use of seaborn pairplot to check the bivariate relation between each pair of attributes and generate a scatter plot
sns.pairplot(iris, hue="Class", markers=["o", "s", "D"])
pl.title('Iris Pair Plot')
pl.savefig('iris_pairplot.png')
pl.show()
