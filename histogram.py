import numpy as np
import cv2

#
cv2.imshow("aslan.png",aslan)

aslan_gri=cv2.imread("aslan.png",0)
cv2.imshow("aslan.png",aslan_gri)

cv2.waitKey()


arrSize=256
arrRange=(0,256)

Hist = np.zeros(256)

[w,h]=aslan_gri.shape

for u in range (0,w):
   for v in range (0,h):
       index=aslan_gri[u,v]
       Hist[index]+=1


