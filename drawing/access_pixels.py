import os
import numpy as np
import cv2

cwd = os.path.dirname(os.path.abspath(__file__))
os.chdir(cwd)

img_color = cv2.imread('messi5.jpg')

if img_color is None:
    print('Error: No image exists')
    exit(1)

rows, cols = img_color.shape[:2]

img_gray = np.zeros((rows, cols), np.uint8)

for row in range(rows):
    for col in range(cols):
        B = img_color.item(row, col, 0)
        G = img_color.item(row, col, 1)
        R = img_color.item(row, col, 2)

        gray = int(0.299*R + 0.587*G + 0.114*B)

        img_gray.itemset(row, col, gray)

img_result = cv2.cvtColor(img_gray, cv2.COLOR_GRAY2BGR)

for row in range(286, 332):
    for col in range(338, 390):
        img_result.itemset(row, col, 0,   0) #삐
        img_result.itemset(row, col, 1, 255) #지
        img_result.itemset(row, col, 2,   0) #알

img_display = cv2.hconcat([img_color, img_result])
cv2.imshow('Access Pixels', img_display)
cv2.waitKey(0)
cv2.destroyAllWindows()