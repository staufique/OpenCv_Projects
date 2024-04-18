import cv2
import numpy as np

kernal = np.ones((5,5),np.uint8)
print(kernal)
path = "resources/taufique.png"

img = cv2.imread(path) #original image
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #converted to gray
imgBlur = cv2.GaussianBlur(imgGray,(5,5),0) #it will blur the image

imgCanny = cv2.Canny(imgBlur,50,50) #Canny is function that use to show the images edges
imgDilates = cv2.dilate(imgCanny,kernal,iterations=1) #it highlights the edges of our image
imgEroded = cv2.erode(imgDilates,kernal,iterations=1) #it will highlight the objects

cv2.imshow("original",img)
cv2.imshow("gray",imgGray)
cv2.imshow("blur",imgBlur)
cv2.imshow("canny",imgCanny)
cv2.imshow("dilation",imgDilates)
cv2.imshow("erosion",imgEroded)

cv2.waitKey(0)