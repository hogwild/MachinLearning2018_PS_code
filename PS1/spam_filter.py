#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 19 13:45:42 2018

@author: xg7
"""



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
            for w in word_list[1:]:
                words[w] = words.get(w, 0) + 1
            email = f.readline()
        word_list = []
        for k, v in words.items():
            if v > self.minNum_words:
                self.word_list.append(k) 
        print("The length of the word list: {}".format(len(self.word_list)))
        print("The word list has been updated.")
                
    def _feature_vector(self, email):
        vec = [0 for i in range(len(self.word_list))]
        for i, w in enumerate(self.word_list):
            if w in email:
                vec[i] = 1
        return vec
        
    def preceptron_train(self, train_filename):
        t = 1
        w = [0 for i in range(len(self.word_list))]
        k = 0
        converge = False
        f = open(train_filename, 'r')
        data = f.readlines()
        while not converge:
            k_per_iter = 0
            for email in data:
                words = email.split()
                label = int(words[0])
                if label == 0:
                    label = -1
                fea = self._feature_vector(words[1:]) # Note: to remove the label
                inner_prod = 0
                for i in range(len(w)):
                    inner_prod += w[i]*fea[i]
                if inner_prod >= 0:
                    pred = 1
                else:
                    pred = -1
                if label*pred < 0:
                    k += 1
                    k_per_iter += 1
                    for j in range(len(w)):
                        w[j] += label*fea[j]
            print("in {}_th iteration, the number of updates: {} ".format(t, k_per_iter))
            if k_per_iter == 0:
                converge = True
            if not converge:
                t += 1
        self.filter['preceptron'] = [w, k, t]
        return w, k, t
    
    def error_rate(self, test_filename):
        f = open(test_filename)
        emails = f.readlines()
        error = 0
        for email in emails:
            words = email.split()
            label = int(words[0])
            if label == 0:
                label = -1
            fea = self._feature_vector(words[1:])
            inner_prod = 0
            for i in range(len(self.word_list)):
                inner_prod += self.filter['preceptron'][0][i]*fea[i]
            if inner_prod*label < 0:
                error += 1
        return error/len(emails)


if __name__ == "__main__":
    perceptron_filter = Spam_filter(minNum_words=20)
    perceptron_filter.get_word_list("train.txt")
    w, k, t = perceptron_filter.preceptron_train("train.txt")
    error_rate = perceptron_filter.error_rate("validation.txt")
    print ("The error rate is: {}".format(round(error_rate, 3)))
    
      
        