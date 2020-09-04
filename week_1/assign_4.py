#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 14:45:02 2020

@author: kling
"""

#%% Importing packages

import numpy as np

#%% Function

def reduce_size( array, size=3):
    array_height, array_width = array.shape
    result = np.zeros( ( int( array_height /size ) , int( array_width /size ) ) )
    for i in range(result.shape[0]):
        for j in range(result.shape[1]):
            x = i*(size)
            y = j*(size)
            result[ i ][ j ] = np.average( array[ x:x+size, y:y+size ] )
    return(result)