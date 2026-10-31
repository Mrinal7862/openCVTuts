import cv2

img = cv2.imread('images/flower.jpg')
width, height = 400, 400
imgRs = cv2.resize(img, (width, height))
print(imgRs)

cropped = imgRs[0:200, 100:400]

cv2.imshow("image1", img)
cv2.imshow("image2", imgRs)
cv2.imshow("cropped", cropped)
cv2.waitKey(0)