#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 16:06:20 2020

@author: kling
"""

import numpy as np
from scipy.fftpack import fft, ifft

def compression_fft( ar, mode='standard', compress = 1 ):
        
    block_size = 8
    im_height, im_width = np.shape(ar)
    result = np.zeros( ar.shape )
    
    if mode == 'fixed_factor':
        quantization_factor = compress
        for i in range(int(im_height/block_size)):
            for j in range(int(im_width/block_size)):
                block = ar[i*block_size:(i+1)*block_size,j*block_size:(j+1)*block_size]
                block = fft(block)
                block = np.floor(block/quantization_factor)*quantization_factor
                result[i*block_size:(i+1)*block_size,j*block_size:(j+1)*block_size] = (
                    ifft(block) )
                
    if mode == 'highest':
        keep = compress
        for i in range(int(im_height/block_size)):
            for j in range(int(im_width/block_size)):
                block = ar[i*block_size:(i+1)*block_size,j*block_size:(j+1)*block_size]
                block = fft(block)
                index_min = np.argpartition(block,-keep)[:-keep] 
                block[index_min] = 0
                result[i*block_size:(i+1)*block_size,j*block_size:(j+1)*block_size] = (
                    ifft(block ) )
                
    if mode == 'standard':
        quantization_matrix = np.array( 
                [[16 ,   11,    10 ,   16,    24 ,   40 ,   51 ,   61],
                 [12 ,   12,    14 ,   19,    26 ,   58 ,   60 ,   55],
                 [14 ,   13,    16 ,   24,    40 ,   57 ,   69 ,   56],
                 [14 ,   17,    22 ,   29,    51 ,   87 ,   80 ,   62],
                 [18 ,   22,    37 ,   56,    68 ,  109 ,  103 ,   77],
                 [24 ,   35,    55 ,   64,    81 ,  104 ,  113 ,   92],
                 [49 ,   64,    78 ,   87,   103 ,  121 ,  120 ,  101],
                 [72 ,   92,    95 ,   98,   112 ,  100 ,  103 ,   99]])*compress
        for i in range(int(im_height/block_size)):
            for j in range(int(im_width/block_size)):
                block = ar[i*block_size:(i+1)*block_size,j*block_size:(j+1)*block_size]
                block = fft(block)
                block = np.rint( block/quantization_matrix )*quantization_matrix
                result[i*block_size:(i+1)*block_size,j*block_size:(j+1)*block_size] = (
                    ifft(block) )
                
    result = np.array( np.rint(result), np.uint8 )
    return(result)