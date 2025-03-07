import numpy as np 
import cv2 

#draw a circle 

#creating the canvas where we drawing our figuers 

canvas = np.zeros((400,400,3),dtype=np.uint8)
green=(0,256,0)
red=(0,0,256)
blue=(256,0,0)

#draw a line on the canvas
starting_point=(50,50)
ending_point=(100,100)
#cv2.line(image, pointFROM, pointTO, color, thickness of line)
starting_point2=(30,150)
ending_point2=(90,250)
cv2.line(canvas,starting_point,ending_point,green,2)

#drawing rectangle 
cv2.rectangle(canvas,starting_point2,ending_point2,red,-1) #-1 make the rectangle filled

#center of the image 
center = (int(canvas.shape[1]/2),int(canvas.shape[0]/2))


#drawing circle
cv2.circle(canvas,center,10,blue,-1)

cv2.imshow('canvas',canvas)
cv2.waitKey(0)