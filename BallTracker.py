import cv2 as cv
import numpy as np
import time



# Create video element
cap = cv.VideoCapture('RedBall.mp4')


#assign upper and lower values from ColorThresholdTesting
ColorLower = (0, 139, 0)
ColorUpper = (180, 255, 255)
c_data = []
#Capture frame from webcam, perfom processing and display results
while(True):
    #Get webcam frame
    ret, frame = cap.read()

    # convert frame to HSV
    hsv = cv.cvtColor(frame, cv.COLOR_BGR2HSV)

	# construct a mask for the specified color
    mask = cv.inRange(hsv, ColorLower, ColorUpper)
    # Erode small contours
    mask = cv.erode(mask, None, iterations=5)
    # Dilates remaing contours
    mask = cv.dilate(mask, None, iterations=5)

    # Find contours on the mask
    cnts, _ = cv.findContours(mask, cv.RETR_EXTERNAL, cv.CHAIN_APPROX_SIMPLE)

    #This is just for debugging
    # print("Number of Contours found = " + str(len(cnts))) 
    #See if contours are in frame
    try:
        #Iterate through countour and find center (average value)
        
        for c in cnts:
            M = cv.moments(c)
            cX= int(M["m10"] / M["m00"])
            cY = int(M["m01"] / M["m00"])
            # current_time = time.strftime()
            data = (cX, cY)
            print(data)
 
        # create a blank image to draw contours on
        contour_img = np.zeros_like(frame)

        # draw contours on the blank image
        cv.drawContours(contour_img, cnts, -1, (0, 255, 0), 3)


        # add the contours to the original frame
        result = cv.add(frame, contour_img)

        #Draw a circle on center of contour and label it
        cv.circle(contour_img, (cX, cY), 7, (255, 255, 255), -1)
        cv.putText(contour_img, "center", (cX - 20, cY - 20),
        cv.FONT_HERSHEY_SIMPLEX, 0.5, (255, 255, 255), 2)


    # No contour found case
    except:
        pass # sad :(


    # Show original image
    # cv.imshow('frame', result)

    # Display the mask if needed
    cv.imshow('mask', mask)
    # Disp contours
    cv.imshow('Conts', contour_img)

    # Show Image
    #cv.imshow('frame', result)

    
    # break loop with q key press
    if cv.waitKey(1) & 0xFF == ord('q'):
        break

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv.destroyAllWindows()

