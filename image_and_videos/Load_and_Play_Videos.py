import cv2

capture = cv2.VideoCapture("vtest.avi")

while True:

    ret,frame = capture.read()

    if ret is False:breakpoint
    cv2.imshow("Video Frame", frame)
    cv2.waitKey(1)

capture.release()
cv2.destroyAllWindows()