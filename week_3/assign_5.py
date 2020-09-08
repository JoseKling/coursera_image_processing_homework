#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 16:22:16 2020

@author: kling
"""

import numpy as np
from scipy.signal import convolve2d

def normalize( array ):
    rng = np.max(array)-np.min(array)
    result = 255*((array-np.min(array))/rng)
    result = np.array( np.floor( result ), dtype='uint8')
    return(result)

def color_edge( img, thresh = 50 ):
    kernel = np.array( [[-1,-1,-1],[-1,8,-1],[-1,-1,-1]])
    result = np.zeros( img[:,:,0].shape )
    result = result + np.abs( convolve2d(img[:,:,0], kernel, mode='same') )
    result = result + np.abs( convolve2d(img[:,:,1], kernel, mode='same') )
    result = result + np.abs( convolve2d(img[:,:,2], kernel, mode='same') )
    result = normalize( result )
    result[result>thresh] = 255
    return(result)

def better_edge( img, thresh=50 ):
    height, width = img[:,:,0].shape
    result = np.zeros( (height-2, width-2 ) )
    for color in range(3):
        color_edge = np.zeros( (height-2, width-2), float ) 
        grid = np.array( img[:,:,color], float)
        for i in range(1, height-1):
            for j in range(1, width-1):
                color_edge[i-1,j-1] = ( np.abs( grid[i,j]-grid[i-1,j-1] ) +
                                    np.abs( grid[i,j]-grid[i,j-1] ) +
                                    np.abs( grid[i,j]-grid[i+1,j-1] ) +
                                    np.abs( grid[i,j]-grid[i-1,j] ) +
                                    np.abs( grid[i,j]-grid[i+1,j] ) +
                                    np.abs( grid[i,j]-grid[i-1,j+1] ) +
                                    np.abs( grid[i,j]-grid[i,j+1] ) +
                                    np.abs( grid[i,j]-grid[i+1,j+1] ) )
        result = result + color_edge
    result = normalize( result )
    result[result>thresh] = 255
    result[result<=thresh]=0
    return(result)
        
            