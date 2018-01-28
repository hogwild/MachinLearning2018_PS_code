#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 28 00:15:23 2018

@author: hogwild
"""

from sklearn import linear_model
import numpy as np


f = open('normalized.txt', 'r')   
data = f.readline()
X = []
y = []
while data:
    temp = data.split(',')
    for i in range(len(temp)):
        temp[i] = float(temp[i])
    y.append(temp.pop())
    temp.insert(0, 1)
    X.append(temp)
    data = f.readline()
f.close()

lm = linear_model.LinearRegression()
model = lm.fit(X,y)
x = np.array([1, 1.461861257564445, 1.1022051669412318])
x = x.reshape(1, -1)
print(lm.predict(x))



