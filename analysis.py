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
# Iris images and database information : https://en.wikipedia.org/wiki/Iris_flower_data_set
# 
#
# https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/  
# Iris dataset as .csv and headers from https://datahub.io/machine-learning/iris#resource-iris

# pands is one of many open-source libraries available with python. It is useful for data manipulation and analysis.

# install pands on the system (done once in command window)
# pip install pandas 



#import pands and give it the identifier "pd" - use pd to call this library
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time # for delays 
from PIL import Image # to display jpg files 
import os 

# to clear terminal screen; https://www.scaler.com/topics/how-to-clear-screen-in-python/
os.system('cls')
# read in the iris.csv file from local drive 
# reason for \\ in file name -  https://stackoverflow.com/questions/28328052/why-do-i-have-to-use-double-backslashes-for-file-paths-in-code
print("\n\nWelcome to the Fisher's Iris data set analysis program")
#time.sleep(1)
print("Author: Shane Keenan")
#time.sleep(1)
print("Project for semester 1, Programming and Scripting module, HDip in Computing in Data Analytics, Lecturer: Andrew Beatty")
#time.sleep(2)
print("\nThe aim of this project is to explore the capabilites of python to manipulate, analyse, display and plot data\n")
#time.sleep(2)

#read in the csv file from local drive 
''' download iris.csv data file and change this path '''
data = pd.read_csv("C:\\Users\\shane\\Desktop\\pands\\pands-project\\iris.csv")

# tidy up the data - rename the columns with formated titles

#newcols={"sepallength":"Sepal Length [cm]","sepalwidth":"Sepal Width [cm]","petallength":"Petal Length [cm]","petalwidth":"Petal Width [cm]","class":"Species"}
#data.rename(columns=newcols,inplace=True)
# create a list with the colum titles for use in plots 
cols = ['Sepal Length [cm]', 'Sepal Width [cm]', 'Petal Length [cm]', 'Petal Width [cm]', 'Species']
# rename columns numerically so easier to work with. 
data = data.rename(columns = {cols[0]:0, cols[1]:1, cols[2]:2, cols[3]:3})


#display details about the Iris data .shape output a tuple with the number of (rows, columns) 
#print(f'\n\n{type(data.shape)}')
#col0 = newcols["sepallength"]

# define the main menu function 
def mainMenu():
    print("MAIN MENU\n")
    print("What would you like to do with the Iris data set?")
    print("Please chose from the following options:")
    print("\t(s) See description")
    print("\t(d) Display raw data")
    print("\t(a) Statistical analysis ")
    print("\t(p) Plot data")
    print("\t(q) Quit program")
    choice = input("please select (s/d/a/p/q):")
    return choice

def description():
    os.system('cls')
    print("\n\nData set description")
    print('The Iris data set is a multivariate data set collated by British statistician and biologist Ronald Fisher. It was first published in his 1936 paper "The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis." ')
    print(f'The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor) giving a total of {(data.shape[0])} rows of data.')
    print(f'There are {(data.shape[1])} columns containing measurements of the various flower characteractics, {cols[0]},{cols[1]}, {cols[2]},{cols[3]} and {cols[4]}.')
    print('The 3 species of Iris are shown in the figure')
    print('Note: Sepal is any of the outer parts of a flower that enclose and protect the unopened flower bud')
    print('\n\nPlease close figure to return to the main menu\n')
    image1 = Image.open("C:\\Users\\shane\\Desktop\\pands\\pands-project\\Iris_setosa.jpg")
    image2 = Image.open("C:\\Users\\shane\\Desktop\\pands\\pands-project\\Iris_versicolor.jpg")
    image3 = Image.open("C:\\Users\\shane\\Desktop\\pands\\pands-project\\Iris_virginica.jpg")
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3)
    ax1.imshow(image1)
    ax2.imshow(image2)
    ax3.imshow(image3)  
    ax1.axis('off')
    ax2.axis('off')
    ax3.axis('off')
    ax1.set_title("Iris Setosa")
    ax2.set_title("Iris Versicolor")
    ax3.set_title("Iris Virginica")
    ax1.text(0, 1500, 'Source: https://en.wikipedia.org/wiki/Iris_flower_data_set', color='black', fontsize=12, ha='left', va='top', alpha=0.5)
    plt.show()
    #print(f"Image format: {img.format}")
    #print(f"Image size: {img.size}")
    os.system('cls')
    

def display():
    os.system('cls')
    print("\nRaw data display")
    print("Random sample of 10 rows\n")
    print(data.sample(10),end = "\n\n")
    

    input("\n\nPress Enter to return to main menu\n\n")
    os.system('cls')
    # keyboard pause: https://stackoverflow.com/questions/50871649/pause-python-script-wait-for-key-press
    
    #print(data.head())s




def analysis():
    print("data analysis")




def plot():
    print("data plot")




choice = mainMenu()
while choice != "q":
    if choice == "s":
        description()
    elif choice == "d":
        display()
    elif choice == "a":
        analysis()
    elif choice == "a":
        plot()
    else:
        print ("invalid choice")
    choice = mainMenu()

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

#check whether there is missing data in the file 
data.isnull()

'''
print(data.head(10).style.highlight_max(color='lightgreen', axis=0))
print(data.head(10).style.highlight_max(color='lightgreen', axis=1))
print(data.head(10).style.highlight_max(color='lightgreen', axis=None))
'''
sns.pairplot(data,hue="Species")