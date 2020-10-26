import cv2

img = cv2.imread('messi5.jpg', cv2.IMREAD_GRAYSCALE)

cv2.imshow('Lionel Messi in Grayscale', img)

cv2.waitKey(0)
cv2.destroyAllWindows()