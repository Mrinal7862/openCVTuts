import cv2
import numpy as np

img = np.zeros((512,512, 3), np.uint8)
print(img)

img[20:30, 60:100] = 255,122,211

cv2.imshow("shape",img)
cv2.waitKey(0)