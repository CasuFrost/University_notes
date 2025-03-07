import cv2 
import numpy as np

img = cv2.imread('../Data/lena.png')

b,g,r = cv2.split(img)
channels=np.hstack([b,g,r])
cv2.imshow('Lena',channels)
cv2.waitKey(0)

#merge channels together
new = cv2.merge([b,g,r])
cv2.imshow('Lena',new)
cv2.waitKey(0)
