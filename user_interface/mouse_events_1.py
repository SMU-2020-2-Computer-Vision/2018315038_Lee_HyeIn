import cv2
import numpy as np
import random

def mouse_callback(event,x,y,flags,param):
    if event == cv2.EVENT_LBUTTONDBLCLK:
        radius = random.randrange(10,50)
        color = (random.randrange(256),random.randrange(256),random.randrange(256))
        cv2.circle(img_color, (x,y), radius, color,-1)


row = 480
cols = 640
img_color = np.zeros((row,cols,3),np.uint8)

winname = 'Mouse Events'
cv2.namedWindow(winname)

cv2.setMouseCallback(winname,mouse_callback)

while True:
    cv2.imshow(winname, img_color)
    key = cv2.waitKey(1)
    if key == 27: break

cv2.destroyAllWindows()