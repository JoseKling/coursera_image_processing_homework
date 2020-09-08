#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 17:18:12 2020

@author: kling
"""

import cv2 as cv


def capture():
    #%% Capture video from camera

    # define a video capture object 
    cap = cv.VideoCapture(0) 
    
    # Define the codec and create VideoWriter object
    fourcc = cv.VideoWriter_fourcc(*'XVID')
    out = cv.VideoWriter('output.avi', fourcc, 20.0, (640,  480), 0)
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            print("Can't receive frame (stream end?). Exiting ...")
            break
    
        # write the frame
        frame = cv.cvtColor( frame, cv.COLOR_BGR2GRAY)
        out.write(frame)
        cv.imshow('frame', frame)
        if cv.waitKey(1) == ord('q'):
            break
        
    # Release everything if job is finished
    cap.release()
    out.release()
    cv.destroyAllWindows() 
