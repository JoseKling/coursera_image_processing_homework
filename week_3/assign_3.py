#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 10:52:37 2020

@author: kling
"""
#%% Importing Packages

import numpy as np

#%% Function

def non_local_means( img, order=1, n_avg=10):
    size = 1+(2*order) 
    height, width = img.shape
    
#Let's calculate the inner product of each block with each other
    result_height = height-size+1
    result_width = width-size+1
    
    num_blocks = (result_height)*(result_width) 
    
    #This matrix will contain all the inner products
    error = np.ones( (result_height, result_width, n_avg, 3))*(height*width*256)

    #This will be the resulting iimage    
    result = np.zeros((result_height, result_width))
    
    #Each i represents one of the blocks
    for i in range(num_blocks):
        y1 = i//(result_height)
        x1 = i%(result_height)
        #The block i is this block
        block = img[ y1-order:y1-order+1 , x1-order:x1-order+1 ]
        #Now we run throught every other block. We don't need to compute the product with itself
        for j in range(i+1, num_blocks):
            y2 = j//(result_height)
            x2 = j%(result_height)
            compare = img[ y2-order : y2-order+1 , x2-order : x2-order+1 ]
            #Exploiting symmetry for efficiency
            err = np.sum(  (block-compare)**2 )
            if err < np.max( error[y1,x1, :,0]):
                replace = np.argmax( error[y1,x1, :,0] )
                error[y1,x1, replace ,0] = err
                error[y1,x1, replace ,1] = y2
                error[y1,x1, replace ,2] = x2
            if err < np.max( error[x1,x2, :,0]):
                replace = np.argmax( error[y2,x2, :,0] )
                error[y2,x2, replace ,0] = err
                error[y2,x2, replace ,1] = y1
                error[y2,x2, replace ,2] = x1
        #replacing the value of the original pixel by the average of the centers of the most similar blocks
        result[y1,x1] = ( img[y1,x1] + np.sum(
                                     img[ np.array(error[y1,x1,:,1:], int) ]))/(n_avg+1)
    return(result)