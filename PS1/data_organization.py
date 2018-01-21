#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 09:34:30 2018

@author: xg7
"""

#f1 = open('spam_train.txt', 'r')
#f2 = open('spam_test.txt', 'r')
#data_all = f1.readlines() + f2.readlines()
#spam_train_2018 = open("spam_train_2018.txt", 'w')
#spam_test_2018 = open("spam_test_2018.txt", 'w')
#
#count = 0
#for d in data_all:
#    if count < 4500:
#        spam_train_2018.write(d)
#    else:
#        spam_test_2018.write(d)
#    count += 1
#spam_train_2018.close()
#spam_test_2018.close()
    
    
    


f = open('spam_train.txt', 'r')
train_data = open('train.txt', 'w')
validation = open('validation.txt', 'w')
data = f.readline()
count = 0
while data:
#    print(data)
    if count < 4000:
        train_data.write(data)
    else:
        validation.write(data)
    data = f.readline()
    count += 1

train_data.close()
validation.close()

        