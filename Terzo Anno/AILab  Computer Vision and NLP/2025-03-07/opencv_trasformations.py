import cv2 
import numpy as np 

#affine trasformations ar rapresented by 3x3 matrix 

img = cv2.imread('../Data/lena.png')

#for each pixel of the image you get the pixel multiplied by the matrix and get the final position of the pixel

resized = cv2.resize(img,(400,400),interpolation =cv2.INTER_LINEAR)
cv2.imshow('a',resized)
cv2.waitKey(0)


