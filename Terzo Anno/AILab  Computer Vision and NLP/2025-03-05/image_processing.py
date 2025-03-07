import cv2
import numpy as np

#read the image 
img = cv2.imread('01-Data/lena.png')

#access image properties 

print(f'image width : {img.shape[1]}') #access Width
print(f'image height : {img.shape[0]}') #access Height
print(f'image channels : {img.shape[2]}') #access channels


#show image on the screen
cv2.imshow('loaded image',img)
cv2.waitKey(2000)



#write img on disk
cv2.imwrite('lena.jpg',img)

