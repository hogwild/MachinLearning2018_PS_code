#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 08:01:35 2018

@author: xg7
"""

strng = "Mississippi"
alp_hist = {}
for e in strng:
    alp_hist[e] = alp_hist.get(e, 0) + 1
    
print(alp_hist)
