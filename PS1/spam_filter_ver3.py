#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 13:45:42 2018

@author: xg7
"""
import numpy as np



class Spam_filter:
    
    def __init__(self, word_list=[], minNum_words=0):
        self.word_list = word_list
        self.minNum_words = minNum_words
        self.filter = {}
        
    def get_word_list(self, train_filename):
        f = open(train_filename, 'r')
        email = f.readline()
        words = {}
        while email:
            word_list = email.split()
            word_list = set(word_list[1:])
            for w in word_list:
                words[w] = words.get(w, 0) + 1
            email = f.readline()
        word_list = []
        print("The total number of the words:", len(words))
        for k, v in words.items():
            if v >= self.minNum_words:
                self.word_list.append(k) 
        print("The number of the words of X = {} : {}".format(self.minNum_words,len(self.word_list)))
#        print("The word list has been updated.")
                
    def _feature_vector(self, email):
#        vec = [0 for i in range(len(self.word_list))]
        vec = np.zeros((len(self.word_list), 1))
        for i, w in enumerate(self.word_list):
            if w in email:
                vec[i] = 1
        return vec
        
    def preceptron_train(self, train_filename):
        t = 1
        w = np.zeros((1, len(self.word_list)))#[0 for i in range(len(self.word_list))]
        k = 0
        converge = False
        f = open(train_filename, 'r')
        data = f.readlines()
        
#        print("the number of data:",len(data))
        while not converge:
            k_per_iter = 0
            temp = 0
            for email in data:
                temp += 1
                email_words = email.split()
#                print(email_words)
                label = int(email_words[0])
                if label == 0:
                    label = -1
                fea = self._feature_vector(email_words[1:]) # Note: to remove the label
                if sum(fea) == 0:
                    print("a odd point:", temp)
                inner_prod = np.dot(w, fea)
#                if inner_prod == 0:
#                    print("the inner product: {}, the label: {}, the index: {}".format(inner_prod, label, temp))
#                print("the inner product: {}, the label: {}".format(inner_prod, label))
                if inner_prod >= 0:
                    sign = 1
#                elif inner_prod == 0:
#                    if t > 10:
#                        print("in iter: {}, the odd point{}".format(t, temp))
#                    pred = -1
                else:
                    sign = -1
                if label*sign < 0:
#                if label*inner_prod <= 0:
    
                    k += 1
                    k_per_iter += 1
                    w += label*fea.transpose()
            print("in {}_th iteration, the number of updates: {} ".format(t, k_per_iter))
            if k_per_iter == 0:
                converge = True
            if not converge:
                t += 1
        self.filter['perceptron'] = [w, k, t]
        return w, k, t
    
    def error_rate(self, test_filename):
        f = open(test_filename)
        emails = f.readlines()
        error = 0
        for e in emails:
            words = e.split()
            label = int(words[0])
            if label == 0:
                label = -1
            fea = self._feature_vector(words[1:])
            inner_prod = np.dot(self.filter['perceptron'][0], fea)
            
#            inner_prod = 0
#            for i in range(len(self.word_list)):
#                inner_prod += self.filter['preceptron'][0][i]*fea[i]
            if inner_prod*label < 0:
                error += 1
        return error/len(emails)


if __name__ == "__main__":
    perceptron_filter = Spam_filter(minNum_words=20)
    perceptron_filter.get_word_list("train.txt")
    w, k, t = perceptron_filter.preceptron_train("train.txt")
    error_rate = perceptron_filter.error_rate("validation.txt")
    print ("The error rate is: {}".format(round(error_rate, 3)))
    
      
        