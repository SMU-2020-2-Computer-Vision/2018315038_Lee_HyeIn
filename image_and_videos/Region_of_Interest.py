import cv2

img = cv2.imread('messi5.jpg')

ROI = img[286:332, 338:390]

cv2.imshow('Ball', ROI)
cv2.waitKey(0)

cv2.destroyAllWindows()