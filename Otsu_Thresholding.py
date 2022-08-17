import numpy as np
import cv2

image=cv2.imread("Thresholding/ra.jpg",0)

""" 
Otsu thresholding: 
Değerleri kendisi otomatik belirler fakat senin aralığın seçmen gerekir.
(değerlerimiz 0-255 arasında olduğu için 0,255 yazıyoruz.)
"""

#simple thresholding
ret1,thresh1=cv2.threshold(image,127,255,cv2.THRESH_BINARY)

#otsu thresholding
ret2,thresh2=cv2.threshold(image,0,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)



cv2.imshow("orjinal resim",image)
cv2.imshow("simple thresh",thresh1)
cv2.imshow("otsu thresh",thresh2)



cv2.waitKey(0)
cv2.destroyAllWindows()
