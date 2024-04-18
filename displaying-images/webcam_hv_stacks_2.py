import cv2
import numpy as np
from my_utils import stackImages
framewidth = 640
frameheight = 360

cap = cv2.VideoCapture(0) #by defining zero we are using our webcam

while True:
    success , img = cap.read()
    kernal = np.ones((5,5),np.uint8)
    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #converted to gray
    imgBlur = cv2.GaussianBlur(imgGray,(7,7),0) #it will blur the image

    imgCanny = cv2.Canny(imgBlur,100,200) #Canny is function that use to show the images edges
    imgDilates = cv2.dilate(imgCanny,kernal,iterations=2) #it highlights the edges of our image
    imgEroded = cv2.erode(imgDilates,kernal,iterations=2) #it will highlight the objects

    stackImg = stackImages(0.5,([img,imgGray,imgBlur],[imgCanny,imgDilates,imgEroded]))

    cv2.imshow("stacked",stackImg)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break