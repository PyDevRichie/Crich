# -*- coding: utf-8 -*-
"""
Created on Fri Oct  5 16:13:33 2018

@author: Richi
"""

import numpy as np
import argparse
import cv2
import imutils

import os
import locale

from shutil import copyfile


# c:/Users/Richi/Dropbox/Python courses/OCR Document scanner sources/document-scanner/images/

# Initialize variables
locale.setlocale(locale.LC_ALL, 'NL_nl')  # Set the localization to NL

curr_pwd = os.getcwd()  # Prints the working directory
# Hard code the path for now


input_path = 'c:/Users/Richi/Dropbox/Python courses/OCR Document scanner sources/document-scanner/images/'


os.chdir(input_path)
# file_list = sorted(os.listdir(input_path))   # Read in files

"""
ap = argparse.ArgumentParser()
ap.add_argument("-i", "--image", required = True,
help = "Path to the image")
args = vars(ap.parse_args())
"""

image = cv2.imread("page.jpg")
image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
image = imutils.resize(image, height = 500)
cv2.imshow("Original", image)

lap = cv2.Laplacian(image, cv2.CV_64F)
lap = np.uint8(np.absolute(lap))
cv2.imshow("Laplacian", lap)
cv2.waitKey(1)