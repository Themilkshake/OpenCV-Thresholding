import cv2
import numpy as np

image=cv2.imread("Thresholding/valo.jpg",0)


""" 
Simple thresholding
"""
ret,thresh0=cv2.threshold(image,160,255,cv2.THRESH_BINARY)

cv2.imshow("simle_thresh",thresh0)


""" 
Adaptive thresholding
"""

thresh1=cv2.adaptiveThreshold(image,160,255,cv2.ADAPTIVE_THRESH_MEAN_C,cv2.THRESH_BINARY,2,2)
thresh2=cv2.adaptiveThreshold(image,160,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,2,2)

cv2.imshow("mean_adative_threshold",thresh1)
cv2.imshow("gauss_adaptive_threshold",thresh2)



cv2.waitKey(0)
cv2.destroyAllWindows()