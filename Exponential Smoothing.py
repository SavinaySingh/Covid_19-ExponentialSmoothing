#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 14:47:00 2020

@author: savinaysingh
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset=pd.read_csv('covid19_India.csv')
dataset.insert(2,'EMA',0) 

X = dataset.iloc[:,0]
y = dataset.iloc[:,1]
y_EMA=dataset.iloc[:,2].astype(float) 

X = pd.to_datetime(X)
X = X.dt.strftime('%d/%m')

y_EMA[1]=0.5*y[1]+0.5*y[0]
for i in range(2,67):
    y_EMA[i]=0.5*y[i-1]+0.5*y_EMA[i-1]

data={'Next 7 days':[0,0,0,0,0,0,0]}
predict_7 = pd.DataFrame(data) 

predict_7['Next 7 days'][0]=0.5*y_EMA[y_EMA.shape[0]-1]+0.5*y[y_EMA.shape[0]-1]



plt.scatter(X,y)
plt.plot(X,y)
plt.plot(X,y_EMA,color='red')
plt.xticks(X, X, rotation='vertical')
plt.xlabel('Date')
plt.ylabel('Number of cases reported')
plt.show()
