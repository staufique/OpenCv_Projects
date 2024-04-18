import cv2
import numpy as np
from my_utils import stackImages

kernal = np.ones((5,5),np.uint8)
print(kernal)
path = "resources/taufique.png"

img = cv2.imread(path) #original image
imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #converted to gray
imgBlur = cv2.GaussianBlur(imgGray,(7,7),0) #it will blur the image

imgCanny = cv2.Canny(imgBlur,100,200) #Canny is function that use to show the images edges
imgDilates = cv2.dilate(imgCanny,kernal,iterations=2) #it highlights the edges of our image
imgEroded = cv2.erode(imgDilates,kernal,iterations=2) #it will highlight the objects



stackImg = stackImages(0.5,([img,imgGray,imgBlur],[imgCanny,imgDilates,imgEroded]))

cv2.imshow("stacked",stackImg)
cv2.waitKey(0)