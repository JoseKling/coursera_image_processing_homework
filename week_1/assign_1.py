#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 13:10:46 2020

@author: kling
"""

#%% Importing packages

import numpy as np

#%%  Definition of the function

def reduce_colors( ar, num_colors=2 ):
    """
    Parameters
    ----------
    array : numpy.array
        np.uint8 Array of a greyscale image.
    num_colors : int, optional
        Number of color for conversion. Must be a power of 2. The default is 2.

    Returns
    -------
    New array with the converted grayscale values

    """
    
    if ar.dtype != np.uint8:
        raise ValueError('The image is not a np.uint8 type array')
    if len(ar.shape)>2:
        raise ValueError('The image is not grayscale')
    if num_colors % 2 != 0:
        raise ValueError('The number of colors is not a power of 2')
    if num_colors > 256:
        raise ValueError('The number of colors is too high')
        
    level = 256/num_colors
    result = np.array( (ar//level)*level, np.uint8 )
    return( result)