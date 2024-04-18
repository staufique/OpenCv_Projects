import cv2
import numpy as np

img = cv2.imread("resource/king.jpg")
print(img.shape)

width,height = 250,350
"""i got axis from paint app using mouse from image we are using"""
# pts1 = np.float32([[644,277],[221,962],[1169,675],[968,1463]]) #perfect for queen image (image point as A,D,B,C)
# pts2 = np.float32([[0,0],[0,height],[width,0],[width,height]]) 

"""this is the right way to do warp the image"""
pts1 = np.float32([[265,61],[500,109],[179,346],[443,402]]) #perfect for queen image (image point as A,B,C,D)
pts2 = np.float32([[0,0],[width,0],[0,height],[width,height]])
print(pts2)

matrix = cv2.getPerspectiveTransform(pts1,pts2)
print("matrix****",matrix)
imgOutput = cv2.warpPerspective(img,matrix,(width,height))

for x in range(0,4):
    cv2.circle(img,(int(pts1[x][0]),int(pts1[x][1])),10,(0,0,255),cv2.FILLED)
    

re=cv2.resize(img,(500,500))
cv2.imshow("window",re)
cv2.imshow("image output",imgOutput)
cv2.waitKey(0)