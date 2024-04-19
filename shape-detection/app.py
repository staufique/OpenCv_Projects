import cv2
import numpy as np

from my_utils import stackImages

framewidth = 350
frameheight = 300

cap = cv2.VideoCapture(1)
cap.set(3, framewidth)
cap.set(4, frameheight)

def empty(a):
    pass
cv2.namedWindow("parameters")
cv2.resizeWindow("parameters",600,200)
cv2.createTrackbar("Threshold1","parameters",24,255,empty)
cv2.createTrackbar("Threshold2","parameters",50,255,empty)
cv2.createTrackbar("area","parameters",13000,100000,empty)


def getContours(img,imgContour):
    contours, hirarchy = cv2.findContours(img,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_NONE)
    
    for cnt in contours:
        area = cv2.contourArea(cnt)
        areaMin = cv2.getTrackbarPos("area","parameters")
        if area>areaMin:
            cv2.drawContours(imgContour,cnt,-1,(255,0,255),7)
            para1 = cv2.arcLength(cnt,True)
            approx = cv2.approxPolyDP(cnt,0.02*para1, True)
            x, y, w, h = cv2.boundingRect(approx)
            cv2.rectangle(imgContour, (x, y), (x + w, y + h),(0, 255, 0),5)
            cv2.putText(imgContour,"Points:: "+str(len(approx)),(x + w + 20, y + 20), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (0,255,0),2)
            cv2.putText(imgContour,"Area: "+str(int(area)),(x + w + 20, y + 45), cv2.FONT_HERSHEY_COMPLEX, 0.7,
                        (0,255,0),2)
            

while True:

    success , img = cap.read()
    imgContour = img.copy()
    imgBlur = cv2.GaussianBlur(img,(7,7),1)
    imgGray = cv2.cvtColor(imgBlur,cv2.COLOR_BGR2GRAY)

    threshold1 = cv2.getTrackbarPos("Threshold1","parameters")
    threshold2 = cv2.getTrackbarPos("Threshold2","parameters")
    imgCanny = cv2.Canny(imgGray,threshold1,threshold2)
    kernal = np.ones((5,5))
    imgDil = cv2.dilate(imgCanny, kernal, iterations= 1)



    getContours(imgDil,imgContour)

    imgStack = stackImages(0.8,([img,imgGray,imgCanny],[imgDil,imgContour,imgContour]))

    cv2.imshow("window", imgStack)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break