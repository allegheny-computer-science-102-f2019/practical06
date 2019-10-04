#!/usr/bin/env python3
"""imageScanner.py: Program to scan the pixels of images for their RGB data."""

__author__      = "NAME"
__date__        = "4 Oct 2019"

#
# Library installation notes
#
# MatPlotLib
# ref: https://matplotlib.org
# install:
# pip install --user matplotlib
#
# NumPy
# ref: https://docs.scipy.org/doc/numpy-1.10.1/user/install.html
# install:
# pip install --user numpy
# or
# pip3 install --user numpy




def getAvgRGB(ima): # works the image algorithm
    """Scans the whole image and then get an average Red, Green and Blue number for the image"""
    #print("  __getAvgRGB()__")

    counter = 0            #Number of pixels that are almost white
    red_int = 0
    green_int = 0
    blue_int = 0

    for i in range(ima.shape[0]):
        for j in range(ima.shape[1]):
            counter += 1
            red_int = red_int + ima[i,j,0]
            green_int = green_int + ima[i,j,1]
            blue_int = blue_int + ima[i,j,2]

    avgRed_flt = red_int / counter
    avgGreen_flt = green_int / counter
    avgBlue_flt = blue_int / counter

    return [avgRed_flt, avgGreen_flt, avgBlue_flt]
#end of getAvgRGB()



def computeSnow(cam):
    """ Manages the image algorithm to determine the snow coverage"""
    #print("  __computeSnow()__")

#For each pixel:
    countSnow = 0            #Number of pixels that are almost white
    t = 0.75                 #Threshold for almost white-- can adjust between 0.0 and 1.0

    for i in range(cam.shape[0]): # rows
        for j in range(cam.shape[1]): # columns
            #print(i,j,cam[i,j,0],cam[i,j,1],cam[i,j,2])
            #Check if red, green, and blue pixels are > t for each i,j location:
            if (cam[i,j,0] > t) and (cam[i,j,1] > t) and (cam[i,j,2] > t): # the Red Green Blue values (channels of color)
                countSnow = countSnow + 1
    return countSnow

#end of computeSnow()



def computeFoliage(cam):
    """ function to determine an average amount of greenery from plants"""
    #print("  __computeFoliage()__")

## TODO: Edit this function to count the numbers of pixels that (hopefully)
## describe the amount of foliage in the images
## This function will be very similar to the computeSnow() function.

#For each pixel:
    countfoliage = 0            #Number of pixels that are almost white
    #Threshold values for colors -- can adjust between 0.0 and 1.0
    redVal_flt = 0.75
    greenVal_flt = 0.75
    blueVal_flt = 0.75


    for i in range(cam.shape[0]): # rows
        for j in range(cam.shape[1]): # columns
            #print(i,j,cam[i,j,0],cam[i,j,1],cam[i,j,2])
            #Check if red, green, and blue pixels are > t for each i,j location:
            if (cam[i,j,0] > redVal_flt) and (cam[i,j,1] > greenVal_flt) and (cam[i,j,2] > blueVal_flt): # the Red Green Blue values (channels of color)
                countfoliage = countfoliage + 1
    return countfoliage

#end of computeFoliage()



def drawLine():
    """ draws a separator line"""
    print("\t  - - - - - - - - - - - - - - - - - - - - - - - - - - - - -\n")
#end of drawLine()

def main(in_file1,in_file2=None): #
    """Driver function"""
#    print("  __main()__")
    print("\t  Welcome to the image Scanner.")
    print("\t  First Input file is  :",in_file1)
    print("\t  Second Input file is :",in_file2)
    drawLine() # place a separator
    ima1 = plt.imread(in_file1)   #Read in an image
    count1 = 0
    count2 = 0

    count1 = computeSnow(ima1) # count the white pixels
    print("\t  +",in_file1, "| computeSnow(), Snow count is:\n\t\t", count1)

    if in_file2 != None: # do we have a second file entered?
            ima2 = plt.imread(in_file2)   #Read in an image
            count2 = computeSnow(ima2)
            print("\t  +",in_file2, "| computeSnow(), Snow count is:\n\t\t", count2)

    drawLine() # place a separator
    # provide an analysis of the Red, Green and Blue pixels.
    colCount1_list = getAvgRGB(ima1)
    print("\t  +",in_file1, "| getAvgRGB(), the average RGB colors:\n\t\t", colCount1_list)

    if in_file2 != None: # do we have a seond file entered?
           colCount2_list = getAvgRGB(ima2)
           print("\t  +",in_file2, "| getAvgRGB(), the average RGB colors:\n\t\t", colCount2_list)



## TODO:
# Determine the amount of folliage there is in each of the images to check if the desert regions are expanding.
#
# You will need to determine what kinds of green color setting to use. For this, experiment with the code
# and experiment settings that you learn from the getAvgRGB() outputs for the color files (see graphics)
    drawLine() # place a separator
    foliageCount1_list = computeFoliage(ima1)
    print("\t  +",in_file1, "| computeFoliage(), foliage count is :\n\t\t", foliageCount1_list)

    if in_file2 != None: # do we have a seond file entered?
        foliageCount2_list = computeFoliage(ima2)
        print("\t  +",in_file2, "| computeFoliage(), foliage count is :\n\t\t", foliageCount2_list)


    print("\t  Program finished. (finally!!)")
#end of main()


# Below is code to launch the program with filenames as parameters.
##############################################################################
#Import the packages for images and arrays:
import matplotlib.pyplot as plt
import numpy as np
import sys

if __name__ == '__main__':

    if len(sys.argv) == 2:
         main(sys.argv[1])

    elif len(sys.argv) == 3:
         main(sys.argv[1],sys.argv[2])
    else:
         print("\t A program to count pixels in a png file. ")
         print("\t Usage: Program name image1.png image2.png")
         print("\t For example: ./imageScanner.py ../graphics/Feb2011.png ../graphics/Feb2014.png ")
         sys.exit(0)
