# pands-project
Fisher's Iris data set analysis 

Aim - use the Iris data set to explore the capabilites of python to manipulate, analyse, display and plot data and in doing so learn to research, generate good documentation and develop clear and concise code.   

Programming and scripting Project 
submission date : 12th May 2023 

## Before you run the program.. 

Included in the github folder is the Iris data set csv file "iris.csv" along with 3 x .jpg image files (Iris_setosa.jpg, Iris_versicolor.jpg and Iris_virginica.jpg).
These files must be downloaded and saved locally to your hard drive(or any drive). The file path then needs to be changed in the analysis.py program 

for iris.csv - line 60<br>
data = pd.read_csv("C:\\Users\\shane\\Desktop\\pands\\pands-project\\iris.csv")

for .jpg files - line 90-93 (inside description() function)<br>
image1 = Image.open("C:\\Users\\shane\\Desktop\\pands\\pands-project\\Iris_setosa.jpg")<br>
image2 = Image.open("C:\\Users\\shane\\Desktop\\pands\\pands-project\\Iris_versicolor.jpg")<br>
image3 = Image.open("C:\\Users\\shane\\Desktop\\pands\\pands-project\\Iris_virginica.jpg")<br>

## Program config 

This program was writen in VSCode in conjugution with a Jupyter notebook which is included in the github folder. 
The program is setup in a way to show you some of the capabilities of python to analyse the Iris data set.<br>The program begins with a brief intro and then to the Main Menu tree. This structure was choosen as a way to divide up and nagivate through the various sections of the program. 


### MAIN MENU 

The main menu structure is contained within the fumction mainMenu() and gives the options to select. The menu tree list is shown below. There are sub-menus within the display raw data (submenu_display()) and Scatter plots (submenu_plot()) options which allow the user to, for instance in the case of the Scatter plots, select which attributes that they would like to plot or plot all the data.  

MAIN MENU

What would you like to do with the Iris data set?<br>
Please chose from the following options:<br>
        (s) See description<br>
        (d) Display raw data<br>
        (a) Statistical plotting and analysis  <br>
        (p) Scatter plots<br>
        (q) Quit program<br>
please select (s/d/a/p/q):s<br>


