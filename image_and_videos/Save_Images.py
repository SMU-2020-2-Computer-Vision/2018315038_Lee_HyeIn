import os
import numpy as np
import cv2

cwd = os.path.dirname(os.path.abspath(__file__))

os.chdir(cwd)

capture = cv2.VideoCapture(0)
fourcc = cv2.VideoWriter_fourcc(*'XVID')
writer = cv2.VideoWriter('output.avi', fourcc, 20.0, (640,480))

while(capture.isOpened()):
    ret, frame = capture.read()
    if ret==True:
        writer.write(frame)

        cv2.imshow('frame',frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

capture.release()
writer.release()
cv2.destroyAllWindows()