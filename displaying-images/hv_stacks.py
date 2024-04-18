import cv2
import numpy as np

kernal = np.ones((5,5),np.uint8)
print(kernal)
path = "resources/taufique.png"

img1 = cv2.imread(path,0) #original image
img2 = cv2.imread(path)

img1 = cv2.resize(img1,(0,0),None,0.5,0.5)
img2 = cv2.resize(img2,(0,0),None,0.5,0.5)

img1 = cv2.cvtColor(img1,cv2.COLOR_GRAY2BGR)

hstack = np.hstack((img1,img2))
vstack = np.vstack((img1,img2))

cv2.imshow("horizontal stack",hstack)
cv2.imshow("vertical stack",vstack)

cv2.waitKey(0)