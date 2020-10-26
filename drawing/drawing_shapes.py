import numpy as np
import cv2


img = np.zeros((480, 640, 3), np.uint8)
cv2.line(img, (0, 0), (200, 100), (0, 0, 255), 5)
cv2.rectangle(img, (300, 200), (500, 400), (0, 255, 0), 3)
cv2.circle(img, (100, 300), 40, (0, 255, 255), -1)
cv2.ellipse(img, (500, 300), (100, 50), 0, 0, 180, 255, -1)

pts = np.array([[100, 50], [200, 300], [600, 200], [500, 100]], np.int32)
pts = pts.reshape((-1,1,2))
cv2.polylines(img, [pts], True, (255, 0, 255) , 4)

font = cv2.FONT_HERSHEY_SIMPLEX 
cv2.putText(img, 'OpenCV', (10, 450), font, 4, (255,255,255), 2, cv2.LINE_AA)

cv2.imshow('Drawing', img)
cv2.waitKey(0)
cv2.destroyAllWindows()