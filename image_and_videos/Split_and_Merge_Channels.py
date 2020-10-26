import cv2

img_color =  cv2.imread('RGB.png')

img_B, img_G, img_R = cv2.split(img_color)

img_merged = cv2.merge([img_B, img_G, img_R])
img_split = cv2.hconcat([img_R, img_G, img_B])

cv2.imshow('Split Channels', img_split)
cv2.imshow('Merged Channels', img_merged)
cv2.waitKey(0)

cv2.destroyAllWindows()