import cv2
import os


cwd = os.path.dirname(os.path.abspath(__file__))
os.chdir(cwd)


video_name = 'vtest.avi'
capture = cv2.VideoCapture(video_name)

while True:
    
    ret, frame = capture.read()

    if ret is True:

        cv2.imshow("Video Frame", frame)
        key = cv2.waitKey(1)

        if key == 27: break

        if key == 32:
            key = cv2.waitKey(0)
            if key == 27: break

    if capture.get(cv2.CAP_PROP_POS_FRAMES) == capture.get(cv2.CAP_PROP_FRAME_COUNT):
        capture.open(video_name)

capture.release()

cv2.destroyAllWindows()