#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 13:41:12 2020

@author: kling
"""
#%% Importing packages

import numpy as np
from scipy.signal import convolve2d

#%% Function

def uniform_blur( array, size=(3,3)):
    
    kernel = np.ones(size)
    result = convolve2d(array, kernel, mode='same')
    return(result)
    