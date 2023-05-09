import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import time # for delays 
from PIL import Image # to display jpg files 
import os 


data = pd.read_csv("C:\\Users\\shane\\Desktop\\pands\\pands-project\\iris.csv")

# tidy up the data - rename the columns with formated titles
#cols = ['Sepal Length [cm]', 'Sepal Width [cm]', 'Petal Length [cm]', 'Petal Width [cm]']
#newcols={"sepallength":"Sepal Length [cm]","sepalwidth":"Sepal Width [cm]","petallength":"Petal Length [cm]","petalwidth":"Petal Width [cm]","class":"Species"}
# rename columns
#data = data.rename(columns=newcols)

#data.rename(columns = {cols[0]:0, cols[1]:1, cols[2]:2, cols[3]:3}, inplace=True)


newcols={0:"Sepal Length [cm]",1:"Sepal Width [cm]",2:"Petal Length [cm]",3:"Petal Width [cm]","class":"Species"}
data.rename(columns=newcols,inplace=True)
plt.figure()
#sns.pairplot(data, hue="Species")
