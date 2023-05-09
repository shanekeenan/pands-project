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
#subplot formatting: https://stackoverflow.com/questions/25862026/turn-off-axes-in-subplots
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
print("Project for Programming and Scripting module, HDip in Computing in Data Analytics at ATU Galway with Lecturer, Andrew Beatty")
#time.sleep(1)
print("Author: Shane Keenan\nDate: 12 May 2023")
#time.sleep(2)
print("\nThe aim of this project is to explore the capabilites of python to manipulate, analyse, display and plot data.\n")
#time.sleep(2)

#read in the csv file from local drive 
''' download iris.csv data file and change this path '''
data = pd.read_csv("C:\\Users\\shane\\Desktop\\pands\\pands-project\\iris.csv")

# tidy up the data - rename the columns with formated titles

newcols={"sepallength":"Sepal Length [cm]","sepalwidth":"Sepal Width [cm]","petallength":"Petal Length [cm]","petalwidth":"Petal Width [cm]","class":"Species"}
# rename columns
data = data.rename(columns=newcols)




#display details about the Iris data .shape output a tuple with the number of (rows, columns) 
#print(f'\n\n{type(data.shape)}')
#col0 = newcols["sepallength"]

# define the main menu function 
def mainMenu():
    # tidy up the data - rename the columns with formated titles
    newcols={"sepallength":"Sepal Length [cm]","sepalwidth":"Sepal Width [cm]","petallength":"Petal Length [cm]","petalwidth":"Petal Width [cm]","class":"Species"}
    # rename columns
    data.rename(columns=newcols, inplace=True)

    print("MAIN MENU\n")
    print("What would you like to do with the Iris data set?")
    print("Please chose from the following options:")
    print("\t(s) See description")
    print("\t(d) Display raw data")
    print("\t(a) Statistical plotting and analysis  ")
    print("\t(p) Scatter plots")
    print("\t(q) Quit program")
    choice = input("please select (s/d/a/p/q):")
    return choice

def description():
    os.system('cls')
    print("\n\nData set description")
    print('''The Iris data set is a multivariate data set collated by British statistician and biologist Ronald Fisher. It was first published in his 1936 paper "The use of multiple measurements in taxonomic problems as an example of linear discriminant analysis. 
The data set consists of 50 samples from each of three species of Iris (Iris setosa, Iris virginica and Iris versicolor) giving a total of 150 rows of data.
There are 5 columns of data, 4 columns containing measurements of the various flower characteractics, Sepal Length [cm], Sepal Width [cm], Petal Length [cm] and Petal Width [cm]. The 5th column specifies the species of Iris. The 3 species of Iris are shown in figure 1 along with labels of the pedal and sepal parts of the Iris.
Note: the Sepal is any of the outer parts of a flower that enclose and protect the unopened flower bud and for these Iris are coloured similarly to the pedal.
    \n\nPlease close figure to return to the main menu\n''')
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
    ax2.text(500, 500, 'Sepal', color='white', fontsize=14, ha='left', va='top', alpha=1)
    ax2.text(1400, 1200, 'Pedal', color='white', fontsize=14, ha='left', va='top', alpha=1)
    ax1.text(0, 1500, 'Source: https://en.wikipedia.org/wiki/Iris_flower_data_set', color='black', fontsize=12, ha='left', va='top', alpha=0.5)
    ax1.text(0, 1400, 'Figure 1. Pictures of the 3 Iris species include in the Iris data set (Iris Setosa, Iris Versicolor and Iris Virginica). Labeling indicate the parts of the Iris flower measured in the data set', color='black', fontsize=12, ha='left', va='top', alpha=0.5)
   
    #plt.arrow(2,5,4,2,width=.3, edgecolor='green',facecolor='red',linestyle='--',linewidth=3)
    plt.show()
    #print(f"Image format: {img.format}")
    #print(f"Image size: {img.size}")
    os.system('cls')
    
def submenu_display():
    print("Display sub-menu\n")
    print("What part of raw Iris data set would you like to see?")
    print("Please chose from the following options:")
    print("\t(r) Ramdom sample of 10 rows")
    print("\t(t) Top 10 rows")
    print("\t(f) Full Iris data set")
    print("\t(q) Return to main menu ")
    subchoice = input("please select (r/t/f/q):")
    return subchoice

def display():
    os.system('cls')
    choice1 = submenu_display()
    while choice1 != "q":
        if choice1 == "r":
            print("\nRaw data display")
            print("Random sample of 10 rows\n")
            print(data.sample(10),end = "\n\n")
            input("\n\nPress Enter to return to display sub-menu\n\n")
            os.system('cls')
        elif choice1 == "t":
            print("\nRaw data display")
            print("Top 10 rows\n")
            print(data.head(10),end = "\n\n")
            input("\n\nPress Enter to return to display sub-menu\n\n")
            os.system('cls')
        elif choice1 == "f":
            print("\nRaw data display")
            print("Full data set 150 rows\n")
            pd.set_option('display.max_rows', 150)
            print(data,end = "\n\n")
            input("\n\nPress Enter to return to display sub-menu\n\n")
            os.system('cls')
        else:
            print ("invalid choice")
            os.system('cls')
        choice1 = submenu_display()
    

    input("\n\nPress Enter to return to main menu\n\n")
    os.system('cls')
    # keyboard pause: https://stackoverflow.com/questions/50871649/pause-python-script-wait-for-key-press
    
    #print(data.head())

def analysis():
    os.system('cls')
    print("Statistical analysis\nThe table below shows some statistics for each of the four Iris attributes measured, these include:\nCount: the number of items in each column\nMean: the mean of each column\nstd: the standard deviation\nmin and max: the minimum and maximum values\n25%, 50%, and 75%: the percentiles\n")
    print(data.describe())
    
    input("\n\nPress Enter to see box plot of data\n\n")
    # create a list with the colum titles for use in plots 
    cols = ['Sepal Length [cm]', 'Sepal Width [cm]', 'Petal Length [cm]', 'Petal Width [cm]', 'Species']
    # rename columns numerically so easier to work with. 
    data.rename(columns = {cols[0]:0, cols[1]:1, cols[2]:2, cols[3]:3}, inplace=True)
    print(f'Box plot\nThis statistical data can be visualised using box plots. Here we see the data plotted vertically for each species against the four attributes. The plot shows the range, interquartile range, median, mode, outliers, and all quartiles of the data set.') 
    print('THe red line indicates the median of the data, the green triangle the mean value, open circles indcicate the outlier points')
    # box plots: https://realpython.com/python-statistics/
    
    fig, ax = plt.subplots(2, 2, figsize=(15, 10))
    A = [data[0][data.Species == 'Iris-setosa'], data[0][data.Species == 'Iris-virginica'], data[0][data.Species == 'Iris-versicolor']]
    B = [data[1][data.Species == 'Iris-setosa'], data[1][data.Species == 'Iris-virginica'], data[1][data.Species == 'Iris-versicolor']]
    C = [data[2][data.Species == 'Iris-setosa'], data[2][data.Species == 'Iris-virginica'], data[2][data.Species == 'Iris-versicolor']]
    D = [data[3][data.Species == 'Iris-setosa'], data[3][data.Species == 'Iris-virginica'], data[3][data.Species == 'Iris-versicolor']]
    ax[0, 0].boxplot(A, labels=('Iris-setosa', 'Iris-virginica', 'Iris-versicolor'),vert=False,widths = 0.7, patch_artist=True, showmeans=True, meanprops={'linewidth': 2, 'color': 'red'},medianprops={'linewidth': 2, 'color': 'purple'})
    ax[0, 0].set_title('Sepal length distribution for Iris species')
    ax[0, 0].set_xlabel(cols[0])
    ax[0, 1].boxplot(B, labels=('Iris-setosa', 'Iris-virginica', 'Iris-versicolor'), vert=False,widths = 0.7, patch_artist=True, showmeans=True, meanprops={'linewidth': 2, 'color': 'red'},medianprops={'linewidth': 2, 'color': 'purple'})
    ax[0, 1].set_xlabel(cols[1])
    ax[0, 1].set_title('Sepal width distribution for Iris species')
    ax[1, 0].boxplot(C,labels=('Iris-setosa', 'Iris-virginica', 'Iris-versicolor'), vert=False,widths = 0.7, patch_artist=True, showmeans=True, meanprops={'linewidth': 2, 'color': 'red'},medianprops={'linewidth': 2, 'color': 'purple'})
    ax[1, 0].set_xlabel(cols[2])
    ax[1, 0].set_title('Pedal length distribution for Iris species')
    ax[1, 1].boxplot(D, labels=('Iris-setosa', 'Iris-virginica', 'Iris-versicolor'), vert=False,widths = 0.7, patch_artist=True, showmeans=True, meanprops={'linewidth': 2, 'color': 'red'},medianprops={'linewidth': 2, 'color': 'purple'})
    ax[1, 1].set_xlabel(cols[3])
    ax[1, 1].set_title('Pedal width distribution for Iris species')
    plt.show()
    
    input("\n\nPress Enter to see a histogram plot of data\n\n")
    print(f'Histogram\nPlotting the data in a histogram allows us to easily see the frequency of certain values in the data. Here we again have broken the data into the four attributes. The three species of Iris are displayed in different colours as indicated in the legend.')
    # histogram - same format as box plot 
    fig, ax = plt.subplots(2, 2, figsize=(16, 10))
    A = [data[0][data.Species == 'Iris-setosa'], data[0][data.Species == 'Iris-virginica'], data[0][data.Species == 'Iris-versicolor']]
    B = [data[1][data.Species == 'Iris-setosa'], data[1][data.Species == 'Iris-virginica'], data[1][data.Species == 'Iris-versicolor']]
    C = [data[2][data.Species == 'Iris-setosa'], data[2][data.Species == 'Iris-virginica'], data[2][data.Species == 'Iris-versicolor']]
    D = [data[3][data.Species == 'Iris-setosa'], data[3][data.Species == 'Iris-virginica'], data[3][data.Species == 'Iris-versicolor']]
    ax[0, 0].hist(A, bins = 15, density=True, label=('Iris-setosa', 'Iris-virginica', 'Iris-versicolor'), edgecolor='black')
    ax[0, 0].set_title('Sepal length distribution for Iris species')
    ax[0, 0].legend(loc='upper right')
    ax[0, 0].set_xlabel(cols[0])
    ax[0, 0].set_ylabel('Frequency')
    ax[0, 1].hist(B, bins = 15, label=('Iris-setosa', 'Iris-virginica', 'Iris-versicolor'), edgecolor='black',)
    ax[0, 1].set_title('Sepal width distribution for Iris species')
    ax[0, 1].legend(loc='upper right')
    ax[0, 1].set_xlabel(cols[1])
    ax[0, 1].set_ylabel('Frequency')
    ax[1, 0].hist(C, bins = 15, label=('Iris-setosa', 'Iris-virginica', 'Iris-versicolor'), edgecolor='black',)
    ax[1, 0].set_title('Pedal length distribution for Iris species')
    ax[1, 0].legend(loc='upper right')
    ax[1, 0].set_xlabel(cols[2])
    ax[1, 0].set_ylabel('Frequency')
    ax[1, 1].hist(D, bins = 15, label=('Iris-setosa', 'Iris-virginica', 'Iris-versicolor'), edgecolor='black',)
    ax[1, 1].set_title('Pedal width distribution for Iris species')
    ax[1, 1].legend(loc='upper right')
    ax[1, 1].set_xlabel(cols[3])
    ax[1, 1].set_ylabel('Frequency')
    plt.show()
    input("\n\nPress Enter to return to main menu\n\n")
    os.system('cls')

def submenu_plot():
    print("Plotting sub-menu\n")
    print("What type of plot Iris data set?")
    print("Please chose from the following options:")
    print("\t(h) Histogram")
    print("\t(s) Scatter plot")
    print("\t(q) return to main menu ")
    subchoice = input("please select (s/d/a/p/q):")
    return subchoice

def plot():
    os.system('cls')
    print('Scatter plotting\nPlease select what two attirbutes you would like to plot')
    print('Enter:\n\t0: Sepal length\n\t1:Sepal width\n\t2:Petal length\n\t3:Petal width')
    x = int(input("please enter x-axis variable (0-3):"))
    y = int(input("please enter y-axis variable (0-3):"))
    colors = {'Iris-setosa':'blue', 'Iris-virginica':'green', 'Iris-versicolor':'orange'}
    #plt.scatter(data[0],data[2], c=data['Species'].map(colors), label=['Iris-setosa', 'Iris-virginica', 'Iris-versicolor'], edgecolors='grey')

    for species in set(data['Species']):
        plt.scatter(data.loc[data['Species'] == species, {x}], data.loc[data['Species'] == species, {2}], color=colors[species], label=species, edgecolors='grey')
    
    plt.xlabel(cols[{x}])
    plt.ylabel(cols[{y}])
    plt.title('Iris data scatter plot')
    plt.xlim([4, 8])
    plt.ylim([0, 8])
    plt.legend()
    plt.show() 
    
    choice1 = submenu_display()
    while choice1 != "q":
        if choice1 == "r":
            print("\nRaw data display")
            print("Random sample of 10 rows\n")
            print(data.sample(10),end = "\n\n")
            input("\n\nPress Enter to return to display sub-menu\n\n")
            os.system('cls')
        elif choice1 == "t":
            print("\nRaw data display")
            print("Top 10 rows\n")
            print(data.head(10),end = "\n\n")
            input("\n\nPress Enter to return to display sub-menu\n\n")
            os.system('cls')
        elif choice1 == "f":
            print("\nRaw data display")
            print("Full data set 150 rows\n")
            pd.set_option('display.max_rows', 150)
            print(data,end = "\n\n")
            input("\n\nPress Enter to return to display sub-menu\n\n")
            os.system('cls')
        else:
            print ("invalid choice")
            os.system('cls')
        choice1 = submenu_display()
    

    input("\n\nPress Enter to return to main menu\n\n")
    os.system('cls')
    
    
    
    
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