#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 15:39:57 2020

@author: kling
"""

import numpy as np

def trimm( array ):
    result = np.copy(array)
    result[result>255]=255
    result[result<0]=0
    return(result)

def gaussian_noise( img, variance=25 ):
    if img.dtype != np.uint8:
        img = img*255
    result = ( img + np.random.normal(0, variance, np.shape(img)) )
    result = trimm(result)
    return(np.uint8(result))

def uniform_noise( img, rng=50 ):
    if img.dtype != np.uint8:
        img = img*255
    result = ( img + np.random.uniform(-rng, rng, np.shape(img)) )
    result = trimm(result)
    return(np.uint8(result))

def sum_noise( img, N=10, level=1,mode='gaussian'):
    result = np.zeros(img.shape, float)
    if mode == 'gaussian':
        for i in range(N):
            noise = gaussian_noise( img, variance = 25*level )
            result = result + noise
    
    if mode == 'uniform':
        for i in range(N):
            noise = uniform_noise( img, rng = 50*level )
            result = result + noise
            
    result = result/N
    result = trimm( result )
    return(result)