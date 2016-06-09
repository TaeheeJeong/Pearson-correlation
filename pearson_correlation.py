# Pearson correlation  
# week3 assignment for Data Analysis Tools

"""
Created on Thu Jun 09 07:42:51 2016

@author: Taehee Jeong
"""

# import libraries
import pandas as pd
import numpy as np
import seaborn as sb
import scipy 
import matplotlib.pyplot as plt

#%% Load data
path='C:/Bigdata/Data Analysis and Interpretation/Dataset/GapMinder/'
data = pd.read_csv(path+'gapminder.csv', low_memory=False)

print data.columns

#%% Clean data
data1=data.copy()

#setting variables you will be working with to numeric
data1['alcconsumption'] = pd.to_numeric(data1['alcconsumption'], errors='coerce')
data1['incomeperperson'] = pd.to_numeric(data1['incomeperperson'], errors='coerce')
data1['lifeexpectancy'] = pd.to_numeric(data1['lifeexpectancy'], errors='coerce')

# subset of data
features=['alcconsumption','incomeperperson','lifeexpectancy']
sub1=data1[features]

#sub1.alcconsumption
#sub1.incomeperperson
#sub1.lifeexpectancy


sub1_clean=sub1.dropna()

#sub1_clean.alcconsumption
#sub1_clean.incomeperperson
#sub1_clean.lifeexpectancy
#%% plot data

scat1 = sb.regplot(x="alcconsumption", y="lifeexpectancy", fit_reg=True, data=sub1_clean)
plt.xlabel('alcohol consumption (litres)')
plt.ylabel('life expectancy at birth (years)')
plt.title('Scatterplot for the Association Between alcohol consumption and life expectancy')

scat2 = sb.regplot(x="incomeperperson", y="lifeexpectancy", fit_reg=True, data=sub1_clean)
plt.xlabel('Income per Person(US$)')
plt.ylabel('life expectancy at birth (years)')
plt.title('Scatterplot for the Association Between Income per Person and life expectancy')

#%% Pearson correlation 

print ('association between alcohol consumption and life expectancy')
print (scipy.stats.pearsonr(sub1_clean['alcconsumption'], sub1_clean['lifeexpectancy']))

print ('association between Income per Person and life expectancy')
print (scipy.stats.pearsonr(sub1_clean['incomeperperson'], sub1_clean['lifeexpectancy']))

