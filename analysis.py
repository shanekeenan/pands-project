# analysis.py  
# pands project   
# Author: Shane Keenan
# Status: ongoing 


'''  Problem statement
This project concerns the well-known Fisher’s Iris data set [3]. 
You must research the data set and write documentation and code (in Python [1]) to investigate it.
An online search for information on the data set will convince you that many people have investigated it previously. 

You are expected to be able to break this project into several smaller tasks that are easier to solve,
and to plug these together after they have been completed. 

You might do that for this project as follows:

1. Research the data set online and write a summary about it in your README. 
2. Download the data set and add it to your repository. 
3. Write a program called analysis.py that: 
1. Outputs a summary of each variable to a single text file, 
2. Saves a histogram of each variable to png files, and 
3. Outputs a scatter plot of each pair of variables. 
4. Performs any other analysis you think is appropriate


You may produce a Jupyter notebook as well containing all your comment.
This notebook should only contain text that you have written yourself, (it may contain referenced code from other sources). 
I will harshly mark any text (not code) that I feel is not written directly by you. 
I want to know what YOU think, not some third party. 

It might help to suppose that your manager has asked you to investigate the data set, with a 
view to explaining it to your colleagues. Imagine that you are to give a presentation on the 
data set in a few weeks’ time, where you explain what investigating a data set entails and how 
Python can be used to do it. 
You have not been asked to create a deck of presentation slides, 
but rather to present your code and its output to them. 

'''

# Resources used: 
# 
#
#
# https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/  
# Iris dataset as .csv and headers from https://datahub.io/machine-learning/iris#resource-iris

# pands is one of many open-source libraries available with python. It is useful for data manipulation and analysis.

# install pands on the system (done once in command window)
# pip install pandas 


#import pands and give it the identifier "pd" - use pd to call this library

import pandas as pd

# read in the iris.csv file from local drive 
# reason for \\ in file name -  https://stackoverflow.com/questions/28328052/why-do-i-have-to-use-double-backslashes-for-file-paths-in-code

data = pd.read_csv("C:\\Users\\shane\\Desktop\\pands\\pands-project\\iris.csv")


print("\n\n\t\t\t Welcome to the Fisher's Iris data set analysis program")
print("\n\t\t Aim - project to explore the capabilites of python to manipulate, analyse, display and plot data")

print("\n\t\t\t Author: Shane Keenan - with acknowledgement to the help given from the vast python community")

print("\nPlease select from the following options")





#what type of data is read in
print(type(data))

# displays the top rows of the dataset -default value of 5 rows - 
print(data.head(10))
print(type(data.head(10)))

# displays a random sample of rows of the dataset -default value of 1 rows - 
print(data.sample(10))
print(type(data.sample(10)))

# displays the header / column data (if there) - this dataset does have a index in the .csv file.  
print(f'\n\n{data.columns}')
print(type(data.columns))


# display the shape of the data set - (rows, columns)
print(f'\n\n{(data.shape)}')
print(f'\n\n{type(data.shape)}')


# to select a certain column of the data and assign it to a variable 

select_data=data[["sepallength","sepalwidth"]]

# 
print(select_data.head(10))

print(type(select_data.head(10)))

# indexing to look at specific rows in the data. 

# to select a row by number index - use iloc[]
print(data.iloc[5])

#to select rows by the attribuete in a certain column index - use loc[]
print(data.loc[data["class"] == "Iris-setosa"])

# and then select a certain column within the subset 
setosa= data.loc[data["class"] == "Iris-setosa"]
select_data=setosa[["sepallength"]]
print(select_data)




# to count number of times a particular class (or any value) has occurred - use value_counts 

print(data["sepallength"].value_counts())

# calculate some statistics of the data - Sepallength

sum_data = data["sepallength"].sum()
mean_data = data["sepallength"].mean()
median_data = data["sepallength"].median()
  
print("Sum: {:.2f} \nMean: {:.2f} \nMedian: {:.2f}".format(sum_data,mean_data,median_data))


# determine the minimum and maximum from a column 
min_data=data["sepallength"].min()
max_data=data["sepallength"].max()
  
print("Minimum:",min_data, "\nMaximum:", max_data)



# rename the columns and formating them 

newcols={"sepallength":"Sepal Length [cm]","sepalwidth":"Sepal Width [cm]","petallength":"Petal Length [cm]","petalwidth":"Petal Width [cm]","class":"Species"}
 
data.rename(columns=newcols,inplace=True)
  
print(data.head())


