import cv2
import os

cwd = os.path.dirname(os.path.abspath(__file__))
os.chdir(cwd)

img = cv2.imread('messi5.jpg')

if img is None:
    print('Error: No image exists')
    exit(1)

while True:

    cv2.imshow('Lionel Messi', img)

    key = cv2.waitKey(1)

    if key == ord('x'):
        img = cv2.flip(img,0)
    elif key == ord('y'):
        img = cv2.flip(img,1)
    elif key == 27:
        break
cv2.destroyAllWindows()  