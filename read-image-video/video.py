import cv2

framewidth = 640
frameheight = 360

cap = cv2.VideoCapture("resources/test.mp4") #here we are using our default video
# cap = cv2.VideoCapture(0) #by defining zero we are using our webcam

# cap.set(3,framewidth) #defining camera width 3 represents width
# cap.set(4,frameheight) #defining camera height 4 represents height
while True:
    success , img = cap.read()

    img = cv2.resize(img,(framewidth,frameheight)) # here we are resizing our video

    cv2.imshow("window",img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break