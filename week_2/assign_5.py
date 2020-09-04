#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 17:14:07 2020

@author: kling
"""
#%% Importing packages

import numpy as np

#%% Function

def err_predict( img, mode='corner', hist=False):
    img = img.astype(float)
    predict = np.copy(img)
    height, width = img.shape
    
    if mode == 'corner':
        for i in range(1, height):
            for j in range(1,width):
                predict[i,j] = np.rint( ( img[i-1,j]+img[i-1,j-1]+img[i,j-1] )/3 )
    
    if mode == 'up':
        for i in range(1, height):
            for j in range(1,width):
                predict[i,j] = img[i-1,j]
    
    if mode == 'left':
        for i in range(1, height):
            for j in range(1,width):
                predict[i,j] = img[i,j-1]

    error = np.abs( predict[1:,1:] - img[1:, 1: ] )
    error = error.flatten()
    if hist == 'True':
        return( error )
    else:
        total = error.size
        prob = error/total
        entropy = -1*np.sum( prob * np.log2(prob, where=(prob!=0)) )
        return( entropy )   
