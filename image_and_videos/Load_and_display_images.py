import cv2
import os


cwd = os.path.dirname(os.path.abspath(__file__))
os.chdir(cwd)

img = cv2.imread('messi5.jpg')

cv2.imshow('Lionel Messi', img)

cv2.waitKey(0)
cv2.destroyAllWindows()