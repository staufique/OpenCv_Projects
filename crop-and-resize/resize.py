import cv2

img = cv2.imread("resources/taufique.png")

print(img.shape)

width,height=400,400

imageResize = cv2.resize(img,(width,height))
print(imageResize.shape)

cv2.imshow("window",img)
cv2.imshow("resized",imageResize)
cv2.waitKey(0)