import cv2
import numpy as np


framewidth = 640
frameheight = 360

# cap = cv2.VideoCapture("resources/test.mp4") #here we are using our default video
cap = cv2.VideoCapture(0)

while True:
    success , img = cap.read()
    kernal = np.ones((5,5),np.uint8)

    imgGray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY) #converted to gray
    imgBlur = cv2.GaussianBlur(imgGray,(5,5),0) #it will blur the image
    imgCanny = cv2.Canny(imgBlur,50,50) #Canny is function that use to show the images edges
    imgDilates = cv2.dilate(imgCanny,kernal,iterations=1) #it highlights the edges of our image
    imgEroded = cv2.erode(imgDilates,kernal,iterations=1) #it will highlight the objects

    """now we are going to resize all the image same"""
    scale = 0.5
    img = cv2.resize(img,(0,0),None,scale,scale)
    imgGray = cv2.resize(imgGray,(0,0),None,scale,scale)
    imgBlur = cv2.resize(imgBlur,(0,0),None,scale,scale)
    imgCanny = cv2.resize(imgCanny,(0,0),None,scale,scale)
    imgDilates = cv2.resize(imgDilates,(0,0),None,scale,scale)
    imgEroded = cv2.resize(imgEroded,(0,0),None,scale,scale)

  

    """here we are making our images as same dimensions so 
    we can add them together in stack"""
    imgGray = cv2.cvtColor(imgGray,cv2.COLOR_GRAY2BGR)
    imgBlur = cv2.cvtColor(imgBlur,cv2.COLOR_GRAY2BGR)
    imgCanny = cv2.cvtColor(imgCanny,cv2.COLOR_GRAY2BGR)
    imgDilates = cv2.cvtColor(imgDilates,cv2.COLOR_GRAY2BGR)
    imgEroded = cv2.cvtColor(imgEroded,cv2.COLOR_GRAY2BGR)


    """here we are making two horizontal stack"""
    hor1 = np.hstack((img,imgGray,imgBlur))
    hor2 = np.hstack((imgCanny,imgDilates,imgEroded))

    """we are adding both horizontal stack into one vertical stack"""
    ver = np.vstack((hor1,hor2))

    cv2.imshow("window",ver)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break