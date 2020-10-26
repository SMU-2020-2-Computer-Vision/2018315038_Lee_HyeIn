import cv2

img_color = cv2.imread('messi5.jpg')

img_gray = cv2.cvtColor(img_color, cv2.COLOR_BGR2GRAY)
cv2.imwrite('messi5_gray.jpg', img_gray)

cv2.imshow('Color Image', img_color)
cv2.imshow('Gray Image', img_gray)
cv2.waitKey(0)

cv2.destroyAllWindows()