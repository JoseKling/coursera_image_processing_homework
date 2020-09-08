#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 10:31:51 2020

@author: kling
"""

import numpy as np

def normalize( array ):
    rng = np.max(array)-np.min(array)
    result = 255*((array-np.min(array))/rng)
    result = np.array( np.floor( result ), dtype='uint8')
    return(result)