import cv2 as cv
import numpy as np

# Create video element
video = cv.VideoCapture(0)

ColorLower = (2, 40, 38)
ColorUpper = (11, 199, 255)

#Capture frame from video and display it on screen
while(True):
    ret, frame = video.read()

    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

	# construct a mask for the specified color, then perform
	# a series of dilations and erosions to remove any small
	# blobs left in the mask

    mask = cv.inRange(hsv, ColorLower, ColorUpper)
    mask = cv.erode(mask, None, iterations=2)
    mask = cv.dilate(mask, None, iterations=2)
    cnts, _ = cv.findContours(mask.copy(), cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)
    print("Number of Contours found = " + str(len(cnts))) 
    
    # create a blank image to draw contours on
    contour_img = np.zeros_like(frame)

    # draw contours on the blank image
    cv.drawContours(contour_img, cnts, -1, (0, 255, 0), 3)

    # add the contours to the original frame
    result = cv.add(frame, contour_img)


    # cv.imshow('frame', result)

    # Display the mask if needed
    cv.imshow('mask', mask)
    cv.imshow('Conts', contour_img)


    # break loop with q key press
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
video.release()
# Destroy all the windows
cv.destroyAllWindows()