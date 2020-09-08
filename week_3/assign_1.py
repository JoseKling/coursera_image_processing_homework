#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep  6 23:46:08 2020

@author: kling
"""

import numpy as np
from normalization import normalize

def hist_equal( img, norm=True ):
    img = normalize(img)
    result = np.copy( img )
    size = img.size
    for value in range(256):
        result[img==value] = 255*(np.sum(img<=value)/size)
        if norm==True:
            result = normalize(result)
    return(result)