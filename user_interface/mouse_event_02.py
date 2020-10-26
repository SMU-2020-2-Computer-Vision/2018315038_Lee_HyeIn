import numpy as np
import cv2
import random

mouse_is_pressed = False
mouse_start_x = -1
mouse_start_y = -1
color = (255,255,255)

def mouse_callback(event,x,y,flags,param):
    global mouse_is_pressed,mouse_start_x,mouse_start_y,color

    if event == cv2.EVENT_LBUTTONDOWN:
        mouse_is_pressed = True
        mouse_start_x = x
        mouse_start_y = y

        color = (random.randrange(256), random.randrange(256), random.randrange(256))
    
    elif event == cv2.EVENT_LBUTTONUP:
        mouse_is_pressed = False
        cv2.rectangle(img_color,(mouse_start_x,mouse_start_y),(x,y),color,-1)

rows = 480
cols = 640
img_color = np.zeros((rows,cols,3),np.uint8)

winname = 'Mouse Events'
cv2.namedWindow(winname)

cv2.setMouseCallback(winname, mouse_callback)

while True:
    cv2.imshow(winname, img_color)
    key = cv2.waitKey(1)
    if key == 27: break

cv2.destroyAllWindows()
