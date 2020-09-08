#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 17:37:59 2020

@author: kling
"""
import cv2 as cv
import numpy as np

def hist_equal( array, norm=True ):
    result = np.copy( array )
    size = array.size
    for value in range(256):
        result[array==value] = 255*(np.sum(array<=value)/size)
    if norm==True:
        result = normalize(result)
    return(result)

def normalize( array ):
    rng = np.max(array)-np.min(array)
    result = 255*((array-np.min(array))/rng)
    result = np.array( np.floor( result ), dtype='uint8')
    return(result)

def equal_frame( file_name ):

    cap = cv.VideoCapture(file_name)
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter('equal_frame.avi', fourcc, 20.0, (640,  480),0)
    
    while cap.isOpened():
        ret, frame = cap.read()
        # if frame is read correctly ret is True
        if not ret:
            print("Stream end.")
            break
        frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        frame = hist_equal(frame)
        out.write(frame)
        if cv.waitKey(1) == ord('q'):
            break
    
    out.release()
    cap.release()
    cv.destroyAllWindows()
    
def equal_all( file_name ):
    
    cap = cv.VideoCapture(file_name)
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter('equal_all.avi', fourcc, 20.0, (640,  480),0)
    
    buffer = np.zeros((20, 480, 640))
    
    while True:
        for i in range(20):
            ret, frame = cap.read()
            if not ret:
               break
            frame = cv.cvtColor( frame, cv.COLOR_BGR2GRAY)
            buffer[i,:,:] = frame
        if not ret:
               print("Stream end.")
               break
        buffer = hist_equal(buffer)
        for i in range(20):
            frame = buffer[i,:,:]
            out.write( frame )
        
    
    out.release()
    cap.release()