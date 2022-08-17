import cv2
import numpy as np


resim=cv2.imread("Thresholding/ra.jpg",0)


"""
 2 çıktı(değişken) döndürdüğü için iki tane yazıyoruz.
"""
"""
birinci,ikinci=cv2.threshold(görüntü,en düşük değer(yukarıda tek kanallı yaptık),
en yüksek değer,cv2.THRESH_BINARY)
"""

ret,threshold1=cv2.threshold(resim,150,250,cv2.THRESH_BINARY)
ret,threshold_inverted=cv2.threshold(resim,150,250,cv2.THRESH_BINARY_INV)

ret,threshold_truncate=cv2.threshold(resim,150,250,cv2.THRESH_TRUNC)

ret,threshold_tozero=cv2.threshold(resim,150,250,cv2.THRESH_TOZERO)
ret,threshold_tozero_inverted=cv2.threshold(resim,150,250,cv2.THRESH_TOZERO_INV)



""" 
binary threshold(ikili eşik ayarlama)
1.Satır: binary threshold(ikili eşik ayarlama)

2.Satır: 1.satırın inverted'i(tam tersi - seçilmişler seçilmiyor, 
         seçilmemişler seçiliyor).
        
3.Satır: Truncate:
Belirlenen eşik değerinden büyük ya da küçük olanlar eşik değerine eşitlenir,
diğer değerlere bir şey yapılmaz.

4.Satır: Thresh to zero(0 eşik değeri):
Belirilenen eşikten düşük olanlar sıfırlanır(yüksek olanlar aynı kalır).


5.Satır: to zero inverted(Tersine dönmüş 0 eşiği):
Eğer piksel değeri eşikten büyükse sıfırlanır (4.satırın tam tersi)(düşük olanlar aynı kalır).

"""



cv2.imshow("thresholding",threshold1)
cv2.imshow("threshold_inverted",threshold_inverted)
cv2.imshow("threshold_truncate",threshold_truncate)
cv2.imshow("threshold_tozero",threshold_tozero)
cv2.imshow("threshold_tozero_inverted",threshold_tozero_inverted)

cv2.imshow("ORJİNAL",resim)



cv2.waitKey(0)
cv2.destroyAllWindows()