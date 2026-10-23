import cv2

frameWidth=640
frameHeight=360

cap = cv2.VideoCapture("noir_.mp4")
# cap.set(3, frameWidth)
# cap.set(4, frameHeight)

while True:
    success,img = cap.read()
    img = cv2.resize(img, (frameWidth, frameHeight ))
    img = cv2.imshow("Video", img)

    if cv2.waitKey(1) &  0xFF == ord('q'):
        break