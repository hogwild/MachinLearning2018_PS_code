#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 09:57:05 2018

@author: xg7
"""

def words(file_name, n_word):
    f = open(file_name, 'r')
    email = f.readline()
    words = {}
    while email:
        word_list = email.split()
        for w in word_list[1:]:
            words[w] = words.get(w, 0) + 1
        email = f.readline()
    word_list = []
    for k, v in words.items():
        if v > n_word:
            word_list.append(k)  
    return word_list


def feature_vector(email, w_lst):
    w_email = email.split()
    w_email = w_email[1:] # remove the label
    vec = [0 for i in range(len(w_lst))]
    for i, w in enumerate(w_lst):
        if w in w_email:
            vec[i] = 1
    return vec


def preceptron_train(data, w_list):
    t = 1
    w = [0 for i in range(len(w_list))]
    k = -1
    while k != 0:
        k = 0
        for email in data:
            words = email.split()
            label = int(words[0])
            if label == 0:
                label = -1
            fea = feature_vector(email, w_list)
            inner_prod = 0
            for i in range(len(w)):
                inner_prod += w[i]*fea[i]
            if inner_prod >= 0:
                pred = 1
            else:
                pred = -1
            if label*pred < 0:
                k += 1
                for j in range(len(w)):
                    w[j] += label*fea[j]
        print("in {}_th iteration, the number of updates: {} ".format(t, k))
        if k > 0:
            t += 1
    return w, k, t


def preceptron_error(w, data, w_list):
    error = 0
    for email in data:
        words = email.split()
        label = int(words[0])
        if label == 0:
            label = -1
        fea = feature_vector(email, w_list)
        inner_prod = 0
        for i in range(len(w)):
            inner_prod += w[i]*fea[i]
        if inner_prod*label < 0:
            error += 1
    return error/len(data)
     
    
if __name__ == '__main__':
    import pickle
    
    f = 'train.txt'
    n = 20
    w_lst = words(f, n)
    emails = open(f, 'r')
    e = emails.readlines()
    print("There are {} training samples.".format(len(e)))
    fea = feature_vector(e[0], w_lst)
    print('the number of none-zero elements: {}, the length: {}'.format(sum(fea), len(fea)))
    try:
        pickle.load(open('k.pk', 'rb'))
    except:
        w, k , t = preceptron_train(e, w_lst)
    f = 'validation.txt'
    valid_data = open(f, 'r')
    e = valid_data.readlines()
    error_rate = preceptron_error(w, e, w_lst)
    print("The error rate is {}".format(round(error_rate, 3)))