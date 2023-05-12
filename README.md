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

The main menu structure is contained within the fumction mainMenu() and gives the options to select. The menu tree list is shown below. 

MAIN MENU

What would you like to do with the Iris data set?<br>
Please chose from the following options:<br>
        (s) See description<br>
        (d) Display raw data<br>
        (a) Statistical plotting and analysis  <br>
        (p) Scatter plots<br>
        (q) Quit program<br>
please select (s/d/a/p/q):s<br>

### Operating instructions

From the main menu tree, there is 5 options as shown. There are sub-menus within option (d) display raw data (submenu_display()) and (p) Scatter plots (submenu_plot()) 

(s) See descritpion (description()) - contains information on the data set orgin and structure. This fucntion also calls and plots the 3 Iris .jpg images side by side as examples of the flowers included in the data set showing the petal and sepal parts of the flower. 

(d) Display raw data (display()) - first brings the user to a display submenu (display_submenu()) which gives 3 options to either (1) display a random selection of 10 rows (2) display the top 10 rows or (3) show the full Iris dataset.  

(a) Statistical plotting and analysis (analysis()) - calls the describe() function which gives a statistical analysis of each data column.Pressing enter will then plot and display 4 boxplots for each of the 4 attribues in the data set and describe its function. Subequently pressing enter will plot and display 4 histograms showing the freqency of each attribute for each flower species. Lastly pressing enter the program will generate a heatmap of the data set showing the level of correlation between the various attributes. 

(p) Scatter plots (plot()) - this option brings you to the plot sub menu from where the user can select one of two options. First option is to plot any two user selected attributes. Any attribute can be plotted on either the x or y axis of the scatter plot. 
second option is to plot a large sub plot structured in a 4 x 4 matrix. 

### file list 

the github directory contains <br>
- analysis.py <br>
- iris data set analysis notebook.jpynb<br>
- Iris_setosa.jpg<br>
- Iris_versicolor.jpg<br>
- Iris_virginica.jpg<br>
- iris.csv<br>
- README.md








