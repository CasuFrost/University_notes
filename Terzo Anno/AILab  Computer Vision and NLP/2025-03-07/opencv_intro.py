import cv2 
import numpy as np

img = cv2.imread('../Data/lena.png')

sub_img = img[:150,:150]

cv2.imshow('image',sub_img)
cv2.waitKey(0)