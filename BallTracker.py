import cv2 as cv
import numpy as np

# Create video element
video = cv.VideoCapture(0)

greenUpper = (179,25,32)
greenLower = (103,10,5,255)
#Capture frame from video and display it on screen
while(True):
    ret, frame = video.read()

    blurred = cv.GaussianBlur(frame, (11, 11), 0)
    hsv = cv.cvtColor(blurred, cv.COLOR_BGR2HSV)
	# construct a mask for the color "green", then perform
	# a series of dilations and erosions to remove any small
	# blobs left in the mask
    mask = cv.inRange(hsv, greenLower, greenUpper)
    mask = cv.erode(mask, None, iterations=2)
    mask = cv.dilate(mask, None, iterations=2)

    cv.imshow('frame',frame)

    # break loop with q key press
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
video.release()
# Destroy all the windows
cv.destroyAllWindows()