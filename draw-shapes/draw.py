import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
print(img)
print(img.shape)

# img[:] = 255,0,0 #coloring our image to blue
# img[100:200,200:400] = 255,0,0 #coloring some particular area

cv2.line(img,(0,0),(img.shape[1],img.shape[0]),(0,255,0),2) #drawing line cv2.line(imagepath,(size),(height,width),(color),(thickness))
cv2.rectangle(img,(300,100),(100,200),(0,0,255),cv2.FILLED) #drawing rectangle
cv2.circle(img,(150,400),50,(255,0,0),cv2.FILLED)
cv2.putText(img,"Drawing Shapes",(75,50),cv2.FONT_HERSHEY_SCRIPT_COMPLEX,1,(0,150,0),1) #adding text to image

cv2.imshow("img",img)
cv2.waitKey(0)