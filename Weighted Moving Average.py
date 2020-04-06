#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr  6 14:36:51 2020

@author: savinaysingh
"""


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# Importing the dataset
dataset=pd.read_csv('covid19_India.csv')
dataset.insert(2,'WMA',0) 

X = dataset.iloc[:,0]
y = dataset.iloc[:,1]
y_WMA=dataset.iloc[:,2]

X = pd.to_datetime(X)
X = X.dt.strftime('%d/%m')

for i in range(3,67):
    y_WMA[i]=0.5*y[i-1]+0.3*y[i-2]+0.2*y[i-3]

data={'Next 7 days':[0,0,0,0,0,0,0]}
predict_7 = pd.DataFrame(data) 

predict_7['Next 7 days'][0]=0.5*y_WMA[y_WMA.shape[0]-1]+0.3*y_WMA[y_WMA.shape[0]-2]+0.2*y_WMA[y_WMA.shape[0]-3]
predict_7['Next 7 days'][1]=0.5*y_WMA[y_WMA.shape[0]-1]+0.3*y_WMA[y_WMA.shape[0]-2]+0.2*predict_7['Next 7 days'][0]
predict_7['Next 7 days'][2]=0.5*y_WMA[y_WMA.shape[0]-1]+0.3*predict_7['Next 7 days'][0]+0.2*predict_7['Next 7 days'][1]

for i in range(3,predict_7.shape[0]):
    predict_7['Next 7 days'][i]=(predict_7['Next 7 days'][i-1]+predict_7['Next 7 days'][i-2]+predict_7['Next 7 days'][i-3])/3



plt.scatter(X,y)
plt.plot(X,y)
plt.plot(X,y_WMA,color='red')
plt.xticks(X, X, rotation='vertical')
plt.xlabel('Date')
plt.ylabel('Number of cases reported')
plt.show()

