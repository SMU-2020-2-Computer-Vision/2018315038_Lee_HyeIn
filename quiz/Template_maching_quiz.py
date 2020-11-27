import numpy as np
import argparse
import imutils
import glob
import cv2

ap = argparse. ArgumentParser ()
ap. add_argument ( "-t" , "--template" , required = True , help = "C:\Users\dlgpd\Documents\Visual Studio 2017\CODE\quiz\exam_background.png" )
ap. add_argument ( "-i" , "--images" , required = True ,
	help = "C:\Users\dlgpd\Documents\Visual Studio 2017\CODE\quiz\fish.png" )
ap. add_argument ( "-v" , "--visualize" ,
args = vars ( ap. parse_args ())

template = cv2.imread(args["template"])
template = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
template = cv2.Canny(template, 50, 200)
(tH, tW) = template.shape[:2]
cv2.imshow("Template", template)
for imagePath in glob.glob(args["images"] + "/*.jpg"):

	image = cv2.imread(imagePath)
	gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
	found = None

	for scale in np.linspace(0.2, 1.0, 20)[::-1]:

		resized = imutils.resize(gray, width = int(gray.shape[1] * scale))
		r = gray.shape[1] / float(resized.shape[1])
		for angle in np.arange(0,360,15):
			rotated = imutils.rotate(image, angle)

			if resized.shape[0] < tH or resized.shape[1] < tW:
				break
			edged = cv2.Canny(resized, 50, 200)
			result = cv2.matchTemplate(edged, template, cv2.TM_CCOEFF)
			(_, maxVal, _, maxLoc) = cv2.minMaxLoc(result)

			if args.get("visualize", False):

				clone = np.dstack([edged, edged, edged])
				cv2.rectangle(clone, (maxLoc[0], maxLoc[1]),
					(maxLoc[0] + tW, maxLoc[1] + tH), (0, 0, 255), 2)
				cv2.imshow("Visualize", clone)
				cv2.waitKey(0)

			if found is None or maxVal > found[0]:
				found = (maxVal, maxLoc, r)

	(_, maxLoc, r) = found
	(startX, startY) = (int(maxLoc[0] * r), int(maxLoc[1] * r))
	(endX, endY) = (int((maxLoc[0] + tW) * r), int((maxLoc[1] + tH) * r))
	
	cv2.rectangle(image, (startX, startY), (endX, endY), (0, 0, 255), 2)
	cv2.imshow("Image", image)
	cv2.waitKey(0)