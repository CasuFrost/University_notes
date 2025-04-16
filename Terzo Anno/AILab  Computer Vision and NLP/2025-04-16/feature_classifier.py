'''an object classifier using image features'''

import cv2 
import numpy as np

#point 1 and 2 : get images

images = []

img1 = cv2.imread('../Data/tomb.jpg')
images.append(img1)

img2 = cv2.imread('../Data/ghost.jpg')
images.append(img2)

img3 = cv2.imread('../Data/dnd.jpg')
images.append(img3)


classes = ['Tomb raider', 'DnD', 'Ghost Impera']

def descriptorsDB(images):
    descriptors_list = []
    orb = cv2.ORB_create(nfeatures=1000)

    for image in images:
        kpt,des = orb.detectAndCompute(image,None)

        