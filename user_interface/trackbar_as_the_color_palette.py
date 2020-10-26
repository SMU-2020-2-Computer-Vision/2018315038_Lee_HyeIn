import numpy as np
import cv2

def do_nothing(x):
    pass

rows = 480
cols = 640
img_color = np.zeros((rows,cols,3), np.uint8)

winname = 'Trackbar as the Color palette'
cv2.namedWindow(winname)

cv2.createTrackbar('R',winname,0,255,do_nothing)
cv2.createTrackbar('G',winname,0,255,do_nothing)
cv2.createTrackbar('B',winname,0,255,do_nothing)

switch = '0 : OFF\n1 : ON'
cv2.createTrackbar(switch,winname,0,1,do_nothing)

while True:
    cv2.imshow(winname, img_color)
    key = cv2.waitKey(1)
    if key == 27:
        break

    R = cv2.getTrackbarPos('R',winname)
    G = cv2.getTrackbarPos('G',winname)
    B = cv2.getTrackbarPos('B',winname)
    S = cv2.getTrackbarPos(switch, winname)

    if S == 0:
        img_color[:]=0

    else:
        img_color[:] = [B,G,R]

cv2.destroyAllWindows()
