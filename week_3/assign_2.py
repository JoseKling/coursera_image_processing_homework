#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 23:50:20 2020

@author: kling
"""

import numpy as np

def median_filter( array, order):
    result = np.copy(array)
    for i in range(order,np.shape(array)[0]-order):
        for j in range(order,np.shape(array)[1]-order):
            result[i][j] = np.median(array[i-order:i+1+order,j-order:j+1+order])
    return(result)