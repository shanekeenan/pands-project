# analysis.py  
# pands project   
# Author: Shane Keenan
# Status: complete
# Resources used: 
# Iris images and database information : https://en.wikipedia.org/wiki/Iris_flower_data_set
# # subplot formatting: https://stackoverflow.com/questions/25862026/turn-off-axes-in-subplots
# https://www.geeksforgeeks.org/python-basics-of-pandas-using-iris-dataset/  
# Iris dataset as .csv and headers from https://datahub.io/machine-learning/iris#resource-iris
# to clear terminal screen; https://www.scaler.com/topics/how-to-clear-screen-in-python/
# pands is one of many open-source libraries available with python. It is useful for data manipulation and analysis.
# reason for \\ in file name -  https://stackoverflow.com/questions/28328052/why-do-i-have-to-use-double-backslashes-for-file-paths-in-code
#  # keyboard pause: https://stackoverflow.com/questions/50871649/pause-python-script-wait-for-key-press
# install pands on the system (done once in command window)
# pip install pandas 

#import libraries with identifiers e.g "pd" for pandas library 
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time # for delays 
from PIL import Image # to display jpg files 
import os 
#intro text 
os.system('cls')
print("\n\nWelcome to the Fisher's Iris data set analysis program")
time.sleep(1)
print("Project for Programming and Scripting module, HDip in Computing in Data Analytics at ATU Galway with Lecturer, Andrew Beatty")
time.sleep(1)
print("Author: Shane Keenan\nDate: 12 May 2023")
time.sleep(1)
print("\nThe aim of this project is to explore the capabilites of python to manipulate, analyse, display and plot data.\n")
time.sleep(1)

#read in the csv file from local drive 
''' download iris.csv data file and change this path '''
data = pd.read_csv("C:\\Users\\shane\\Desktop\\pands\\pands-project\\iris.csv")
# tidy up the data - rename the columns with formated titles
newcols={"sepallength":"Sepal Length [cm]","sepalwidth":"Sepal Width [cm]","petallength":"Petal Length [cm]","petalwidth":"Petal Width [cm]","class":"Species"}
# rename columns
data = data.rename(columns=newcols)
#list with column names for plotting
cols = ['Sepal Length [cm]', 'Sepal Width [cm]', 'Petal Length [cm]', 'Petal Width [cm]']
# define the main menu function 
def mainMenu():
    # tidy up the data - rename the columns with formated titles
    newcols={"sepallength":"Sepal Length [cm]","sepalwidth":"Sepal Width [cm]","petallength":"Petal Length [cm]","petalwidth":"Petal Width [cm]","class":"Species"}
    data.rename(columns=newcols, inplace=True)  # rename columns
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
    plt.show()
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

    input("\n\nPress Enter to see a heatmap correlation plot of the Iris data set\n\n")
    print(f'Heatmap \nHeatmaps are particularly useful for illustrating the covariance and correlation between attributes.')
    print('From the map we can see - Petal width and petal length have high correlations\n-Petal length and sepal width have good correlations.\n-Petal Width and Sepal length have good correlations.')
    print('Conversely, Sepal length and Sepal width are poorly correlated')

    newcols={0:"Sepal Length [cm]",1:"Sepal Width [cm]",2:"Petal Length [cm]",3:"Petal Width [cm]","class":"Species"}
    data.rename(columns=newcols,inplace=True)
    sns.heatmap(data.corr(method='pearson'), annot = True)
    plt.show()



    input("\n\nPress Enter to return to main menu\n\n")
    os.system('cls')

def submenu_plot():
    print("Scatter Plot sub-menu\n")
    print("Please chose from the following options:")
    print("\t(s) Select two variables to plot ")
    print("\t(a) Plot all attributes")
    print("\t(q) return to main menu ")
    subchoice = input("please select (s/a/q):")
    return subchoice
def plot():
    os.system('cls')
    
    choice1 = submenu_plot()
    while choice1 != "q":
        if choice1 == "s":
            os.system('cls')
            data.rename(columns = {cols[0]:0, cols[1]:1, cols[2]:2, cols[3]:3}, inplace= True)
            print('Scatter plotting\nPlease select what two attirbutes you would like to plot')
            print('Enter:\n\t0:Sepal length\n\t1:Sepal width\n\t2:Petal length\n\t3:Petal width')
            x = int(input("please enter x-axis variable (0-3):"))
            y = int(input("please enter y-axis variable (0-3):"))
            colors = {'Iris-setosa':'blue', 'Iris-virginica':'green', 'Iris-versicolor':'orange'}
            #plt.scatter(data[0],data[2], c=data['Species'].map(colors), label=['Iris-setosa', 'Iris-virginica', 'Iris-versicolor'], edgecolors='grey')

            for species in set(data['Species']):
                plt.scatter(data.loc[data['Species'] == species, x], data.loc[data['Species'] == species, y], color=colors[species], label=species, edgecolors='grey')
            plt.xlabel(cols[x])
            plt.ylabel(cols[y])
            plt.title('Iris data scatter plot')
            #plt.xlim([4, 8])
            #plt.ylim([0, 8])
            plt.legend()
            plt.show() 
            os.system('cls')
        elif choice1 == "a":
            newcols={0:"Sepal Length [cm]",1:"Sepal Width [cm]",2:"Petal Length [cm]",3:"Petal Width [cm]","class":"Species"}
            data.rename(columns=newcols,inplace=True)
            plt.figure()
            sns.pairplot(data,hue="Species")
            plt.show()          
            input("\n\nPress Enter to return to display sub-menu\n\n")
            os.system('cls')
        else:
            print ("invalid choice")
            os.system('cls')
        choice1 = submenu_plot()
    input("\n\nPress Enter to return to main menu\n\n")
    os.system('cls')    

choice = mainMenu()
while choice != "q":
    if choice == "s":
        description()
    elif choice == "d":
        display()
    elif choice == "a":
        analysis()
    elif choice == "p":
        plot()
    else:
        print ("invalid choice")
    choice = mainMenu()

print(''' ⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣠⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣤⣤⠀⠀⠀⢀⣴⣿⡶⠀⣾⣿⣿⡿⠟⠛⠁
⠀⠀⠀⠀⠀⠀⣀⣀⣄⣀⠀⠀⠀⠀⣶⣶⣦⠀⠀⠀⠀⣼⣿⣿⡇⠀⣠⣿⣿⣿⠇⣸⣿⣿⣧⣤⠀⠀⠀
⠀⠀⢀⣴⣾⣿⡿⠿⠿⠿⠇⠀⠀⣸⣿⣿⣿⡆⠀⠀⢰⣿⣿⣿⣷⣼⣿⣿⣿⡿⢀⣿⣿⡿⠟⠛⠁⠀⠀
⠀⣴⣿⡿⠋⠁⠀⠀⠀⠀⠀⠀⢠⣿⣿⣹⣿⣿⣿⣿⣿⣿⡏⢻⣿⣿⢿⣿⣿⠃⣼⣿⣯⣤⣴⣶⣿⡤⠀
⣼⣿⠏⠀⣀⣠⣤⣶⣾⣷⠄⣰⣿⣿⡿⠿⠻⣿⣯⣸⣿⡿⠀⠀⠀⠁⣾⣿⡏⢠⣿⣿⠿⠛⠋⠉⠀⠀⠀
⣿⣿⠲⢿⣿⣿⣿⣿⡿⠋⢰⣿⣿⠋⠀⠀⠀⢻⣿⣿⣿⠇⠀⠀⠀⠀⠙⠛⠀⠀⠉⠁⠀⠀⠀⠀⠀⠀⠀
⠹⢿⣷⣶⣿⣿⠿⠋⠀⠀⠈⠙⠃⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠈⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣤⣤⣴⣶⣦⣤⡀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡀⠀⠀⠀⠀⠀⠀⠀⣠⡇⢰⣶⣶⣾⡿⠷⣿⣿⣿⡟⠛⣉⣿⣿⣿⠆
⠀⠀⠀⠀⠀⠀⢀⣤⣶⣿⣿⡎⣿⣿⣦⠀⠀⠀⢀⣤⣾⠟⢀⣿⣿⡟⣁⠀⠀⣸⣿⣿⣤⣾⣿⡿⠛⠁⠀
⠀⠀⠀⠀⣠⣾⣿⡿⠛⠉⢿⣦⠘⣿⣿⡆⠀⢠⣾⣿⠋⠀⣼⣿⣿⣿⠿⠷⢠⣿⣿⣿⠿⢻⣿⣧⠀⠀⠀
⠀⠀⠀⣴⣿⣿⠋⠀⠀⠀⢸⣿⣇⢹⣿⣷⣰⣿⣿⠃⠀⢠⣿⣿⢃⣀⣤⣤⣾⣿⡟⠀⠀⠀⢻⣿⣆⠀⠀
⠀⠀⠀⣿⣿⡇⠀⠀⢀⣴⣿⣿⡟⠀⣿⣿⣿⣿⠃⠀⠀⣾⣿⣿⡿⠿⠛⢛⣿⡟⠀⠀⠀⠀⠀⠻⠿⠀⠀
⠀⠀⠀⠹⣿⣿⣶⣾⣿⣿⣿⠟⠁⠀⠸⢿⣿⠇⠀⠀⠀⠛⠛⠁⠀⠀⠀⠀⠀⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠈⠙⠛⠛⠛⠋⠁⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀''')

print('\n\nThanks for playing Andrew : )\n\n')
