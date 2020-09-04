#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 16:30:29 2020

@author: kling
"""

import cv2 as cv
from assign_1 import compression

def color_jpeg( img, comp1=1, comp2=1 ):
    img = img/255
    result = cv.cvtColor(img, cv.COLOR_RGB2YCR_CB)
    result[:,:,0] = compression( result[:,:,0] )
    result[:,:,1] = compression( result[:,:,1], compress = comp1 )
    result[:,:,2] = compression( result[:,:,2], compress = comp2 )
    result = cv.cvtColor(img, cv.COLOR_YCR_CB2RGB)    
    
    return( result )

