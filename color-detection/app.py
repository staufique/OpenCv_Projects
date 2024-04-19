import cv2
import numpy as np

framewidth = 400
frameheight = 400

cap = cv2.VideoCapture(0) 
cap.set(3,framewidth) #defining camera width 3 represents width
cap.set(4,frameheight) #defining camera height 4 represents height

def empty(a):
    pass
cv2.namedWindow("hsv")
cv2.resizeWindow("hsv",640,240)
cv2.createTrackbar("HUE Min","hsv",0,179,empty)
cv2.createTrackbar("HUE Max","hsv",179,179,empty)
cv2.createTrackbar("SAT Min","hsv",0,255,empty)
cv2.createTrackbar("SAT Max","hsv",255,255,empty)
cv2.createTrackbar("VALUE Min","hsv",0,255,empty)
cv2.createTrackbar("VALUE Max","hsv",255,255,empty)

while True:

    success , img = cap.read()

    imghsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)
    img = cv2.resize(img,(framewidth,frameheight)) # here we are resizing our video

    h_min  = cv2.getTrackbarPos("HUE Min","hsv")
    h_max  = cv2.getTrackbarPos("HUE Max","hsv")
    s_min  = cv2.getTrackbarPos("SAT Min","hsv")
    s_max  = cv2.getTrackbarPos("SAT Max","hsv")
    v_min  = cv2.getTrackbarPos("VALUE Min","hsv")
    v_max  = cv2.getTrackbarPos("VALUE Max","hsv")
    
    lower = np.array([h_min,s_min,v_min])
    upper = np.array([h_max,s_max,v_max])

    mask = cv2.inRange(imghsv,lower,upper)
    mask = cv2.resize(mask, (framewidth, frameheight))

    result = cv2.bitwise_and(img,img,mask=mask)
    
    mask = cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)#making it 3 channels

    hstack = np.hstack([img,mask,result])


    # cv2.imshow("window",img)
    # cv2.imshow("HSV Color Space ",imghsv)
    # cv2.imshow("maks ",mask)
    # cv2.imshow("result ",result)
    cv2.imshow("hstack  ",hstack)
  

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()