# Project 2018 - Programming and Scripting
# Guilherme G. C. Paes - 2018

# After some research I've found out that for the purpose of this project numpy, pandas and matplotlib would be the best libraries to use
# Importing the libraries:
import numpy as np
import pandas as pd
import matplotlib.pyplot as pl

# Importing the dataset from iris.csv file
iris = pd.read_csv("iris.csv", names = ["Sepal Length", "Sepal Width", "Petal Length", "Petal Width", "Class"])
#Printing some data just for visualization
print(iris.sample(10))

# Printing the rows and columns of the data using the shape property:
print("The iris dataset has", iris.shape, "rows and columns respectively")

#Calculating the mean of each column using numpy
print("This is the mean value for each column: \n", np.mean(iris))

#Calculating the max of each column using numpy
print("This is the maximum value for each column: \n",np.max(iris))

#Calculating the min of each column using numpy
print("This is the minimum value for each column: \n",np.min(iris))

#For better visualization, the pandas library shows a better summary of the data, such as mean, max, min, std
print(iris.describe())


# Creating a Histogram of data using matplotlib
iris.hist()
pl.show()
