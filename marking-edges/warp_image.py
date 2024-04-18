import cv2
import numpy as np

"""here we are creating array to save our mouse clicks axis values (x,y)"""
circles = np.zeros((4,2),np.int64) 

"""created counter beacuse we want only 4 edges"""
counter = 0 

def mousePoints(event,x,y,flags,params):
    global counter
    #created mouse left button down event
    if event == cv2.EVENT_LBUTTONDOWN:
        print(x,y)
        #adding our clicks to aour array circles
        circles[counter] = x,y

        #adding +1 on clicks
        counter += 1
        print(circles)

#creating image array
img = cv2.imread("resource/king.jpg")

while True:
    if counter == 4:
        width,height = 250,350

        """this is the right way to do warp the image"""
        pts1 = np.float32([circles[0],circles[1],circles[2],circles[3]]) #click image as A,D,B,C(top_left, bottom_left, top_right, bottom_right) to get desired output
        pts2 = np.float32([[0,0],[0,height],[width,0],[width,height]])

        #without this matrix we cannot warp our image
        #this matrix gets two float array and give use 3d array
        matrix = cv2.getPerspectiveTransform(pts1,pts2)
        #warping our selected image
        imgOutput = cv2.warpPerspective(img,matrix,(width,height))
        #showing warped array
        cv2.imshow("window",imgOutput)
        cv2.waitKey(0)
        break

    for x in range(0,4):
        cv2.circle(img,(int(circles[x][0]),int(circles[x][1])),5,(0,0,255),cv2.FILLED)
    img = cv2.resize(img,(500,500))
    cv2.imshow("window",img)
    cv2.setMouseCallback("window",mousePoints)
    cv2.waitKey(1)