#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 21:18:57 2018

@author: hogwild
"""

import pickle
import matplotlib.pylab as plt
import random
from mpl_toolkits.mplot3d import Axes3D
 



def compute_error(pred, truth):
    error = 0
    n = len(pred)
    for i in range(n):
        error += (pred[i] - truth[i])**2
#        print(error)
    error /=2*n
    return error


def compute_grad(pred_i, truth_i, x):
    grad = []
    
    for x_i in x:
        grad.append((pred_i-truth_i)*x_i)
    return grad


## training with stochastic gradient descent 
def train(X, learning_rate):
    num_iter = 3
    steps = 0
    margin = 0.0001
    error_history = []
    num_dim = len(X[0]) - 1
#    n = len(X)
    w = [0 for i in range(num_dim)]
    while True:
        ## predict and compute error
        random.shuffle(X)
        error = 0
        for x in X:
            pred_y = 0
            y = x[-1]
            for i, x_i in enumerate(x[:-1]):
                pred_y += w[i]*x_i
#                print(temp)
            error += compute_error([pred_y], [y])                
        ## SGD 
            g = compute_grad(pred_y, y, x[:-1])              
            for i in range(num_dim):
                w[i] -= learning_rate*g[i]
        error /= len(X) ## it has been divided by 2 in the compute errors
        error_history.append(error)
        if error <= margin or steps >= num_iter:
            return w, error_history, steps
        steps += 1
        
    


if __name__ == "__main__":
    
## load data
    f = open('normalized.txt', 'r')   
    data = f.readline()
    X = []
#    y = []
    while data:
        temp = data.split(',')
        for i in range(len(temp)):
            temp[i] = float(temp[i])
#        y.append(temp.pop())
        temp.insert(0, 1)
        X.append(temp)
        data = f.readline()
    f.close()
    
#fig = plt.figure()
#ax = fig.add_subplot(111, projection='3d')
    

## regression
    learning_rate = 0.1
    w, error_history, steps = train(X, learning_rate)

## prediction
    f = open('mean_std.pk', 'rb')
    l, b, p = pickle.load(f)
    f.close()
    h = [3150, 4]
    x = [0, 0, 0]
    x[0] = 1
    x[1] = (h[0] - l['mean']) / l['std']
    x[2] = (h[1] - b['mean']) / b['std']
    pred_price = sum([w[i]*x[i] for i in range(3)])
    pred_price = pred_price*p['std'] + p['mean']
   
    
    
    

        
        
            