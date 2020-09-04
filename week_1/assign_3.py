#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 13:45:31 2020

@author: kling
"""

#%% Importing packages

import numpy as np

#%% Function

def rotate( array, angle=90):
    
    height, width = array.shape
    angle = np.pi*angle/180
    new_h = int( np.abs(np.ceil(height*np.cos(angle)+ width*np.sin(angle)) ) )
    new_w = int( np.abs( np.ceil(width*np.cos(angle)+ height*np.sin(angle) ) ) )
    transf = [[np.cos(angle), np.sin(angle)],[-1*np.sin(angle),np.cos(angle)]]
    
    result = np.zeros((new_h, new_w))
    for i in range(height):
        for j in range(width):
            new_coord = np.floor(np.matmul( transf, np.array([i,j]).T ))
            new_y = int(new_coord[0] )
            new_x = int(new_coord[1]+ (height*np.sin(angle)))
            result[new_y, new_x] = array[i,j]
    return(result)