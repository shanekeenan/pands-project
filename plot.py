
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time # for delays 
from PIL import Image # to display jpg files 
import os 


data = pd.read_csv("C:\\Users\\shane\\Desktop\\pands\\pands-project\\iris.csv")

# tidy up the data - rename the columns with formated titles
cols = ['Sepal Length [cm]', 'Sepal Width [cm]', 'Petal Length [cm]', 'Petal Width [cm]']
newcols={"sepallength":"Sepal Length [cm]","sepalwidth":"Sepal Width [cm]","petallength":"Petal Length [cm]","petalwidth":"Petal Width [cm]","class":"Species"}
# rename columns
data = data.rename(columns=newcols)

data.rename(columns = {cols[0]:0, cols[1]:1, cols[2]:2, cols[3]:3}, inplace=True)

os.system('cls')
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
plt.xlim([0, 8])
plt.ylim([0, 8])
plt.legend()
plt.show() 



