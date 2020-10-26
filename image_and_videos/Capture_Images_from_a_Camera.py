import cv2
import os

capture = cv2.VideoCapture(0)

while True:
    ret, frame = capture.read()

    if ret is False:
        print('Error: No image is captured!')
        break

    cv2.imshow("Video Frame", frame)
    key = cv2.waitKey(1)

    if key == 27: break

    if key == 32:
        key = cv2.waitKey(0)
        if key == 27: break

capture.release()

cv2.destroyAllWindows()