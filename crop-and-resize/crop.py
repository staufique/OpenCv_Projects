import cv2

img = cv2.imread("resources/taufique.png")

print(img.shape)

width,height=400,400

imageResize = cv2.resize(img,(width,height))
print(imageResize.shape)

imgCropped = img[50:350,400:700] #we are changing the size of our image 
imgCroppedResize = cv2.resize(imgCropped,(img.shape[1],img.shape[0])) #we getting our original size for cropped image

cv2.imshow("window",img)
cv2.imshow("resized",imageResize)
cv2.imshow("cropped",imgCropped)
cv2.imshow("cropped resize",imgCroppedResize)
cv2.waitKey(0)