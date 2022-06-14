# Author: Nesara Thottethodi
# Test wrapper for extractDatacube

from datacube import *

vidPaths = ["vids/cubetest1.MOV", "vids/cubetest2.MOV"]

# TEST FUNCTION CALL
for vid in vidPaths:
    cube = extractDatacube(vid)
    print("The datacube shape for " + vid + " is " + str(cube.shape))
