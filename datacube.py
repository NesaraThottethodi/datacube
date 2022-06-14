#Nesara Thottethodi
#This function takes a file name of a video (String) as a parameter, and returns the data of that video in a 4D Array

import cv2
import numpy as np


def extractDatacube(vidPath):
    #Gets data from file
    cap = cv2.VideoCapture(vidPath)
    frameList = []

    while(cap.isOpened()):
        #Reads file data in the form of frames (rows and columns, as well as 3 for number of color values in RGB)
        ret, frame = cap.read()
        
        # This condition prevents from infinite looping
        # in case video ends.
        if ret == False:
            break
        
        # Append new frame onto frameList for the video
        frameList.append(frame)
 
    cap.release()
    cv2.destroyAllWindows()

    #Adds frameList as another axis in 3D array of frame, displays the number of frames in index 0 of item
    dataCube = np.stack(frameList,axis=0)
    return dataCube

    # If necessary to switch order of dimensions, uncomment code below
    # foo = dataCube.transpose([3,1,2,0])
    # print(foo.shape)
    



