import cv2
import numpy as np

unchanged_image = cv2.imread('picture.png' , -1)    # it's like using cv2.IMREAD_UNCHANGED
gray_image =      cv2.imread('picture.png' , 0 )    # it's like using cv2.IMREAD_GRAYSCALE
bgr_image =       cv2.imread('picture.png' , 1 )    # it's like using cv2.IMREAD_COLOR

cv2.imshow('unchanged' , unchanged_image)
cv2.imshow('gray' , gray_image)
cv2.imshow('bgr' , bgr_image)

cv2.waitKey(0)
cv2.destroyAllWindows()