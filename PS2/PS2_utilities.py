#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 27 19:51:29 2018

@author: hogwild
"""

def get_mean(x):
    return sum(x)/len(x)


def get_std(x, mean):
    temp = []
    for e in x:
        temp.append((e - mean)**2)
    return (sum(temp)/len(temp))**0.5


def get_mean_and_std(x):
    mean = sum(x)/len(x)
    temp = []
    for e in x:
        temp.append((e - mean)**2)
    std = (sum(temp)/len(temp))**0.5
    return mean, std


def normalization(x, mean, std):
    norm_x = []
    for e in x:
        norm_x.append((e - mean)/std)
    return norm_x
        

def proc_housing_data(filename):
    f = open(filename, 'r')
    living_room_area = []
    number_bedrooms = []
    price = []
    recorder = f.readline()
    while recorder:
        r = recorder.split(",")
        living_room_area.append(int(r[0]))
        number_bedrooms.append(int(r[1]))
        price.append(int(r[2]))
        recorder = f.readline()
## normalization
    l_m, l_std = get_mean_and_std(living_room_area)
    print(l_m, l_std)
    b_m, b_std = get_mean_and_std(number_bedrooms)
    p_m, p_std = get_mean_and_std(price)
    
    normal_living = normalization(living_room_area, l_m, l_std)
    normal_bedroom = normalization(number_bedrooms, b_m, b_std)
    normal_price = normalization(price, p_m, p_std)
    
    f = open("normalized.txt", 'w')
    for i in range(len(normal_price)):
        f.write(str(normal_living[i]) + ','+ str(normal_bedroom[i]) + ',' + \
                str(normal_price[i])+'\n')
    f.close()

    
if __name__ == "__main__":
#    x = [i for i in range(10)]
#    print("the mean is", get_mean(x))
#    print("the std is", get_std(x, get_mean(x)))
#    print("the mean and std are", get_mean_and_std(x))
    proc_housing_data('housing.txt')