import cv2
import numpy as np

def detect_ball(frame):
    # Convert the frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Apply GaussianBlur to reduce noise and help the Hough Circle Transform
    blurred = cv2.GaussianBlur(gray, (9, 9), 2)

    # Use Hough Circle Transform to detect circles
    circles = cv2.HoughCircles(
        blurred, cv2.HOUGH_GRADIENT, dp=1, minDist=500, param1=50, param2=50, minRadius=3, maxRadius=100
    )
    print("Circccccc")
    print(circles)
    ball_detected = False
    ball_center = None

    if circles is not None:
        # Convert the (x, y) coordinates and radius of the circles to integers
        circles = np.round(circles[0, :]).astype("int")

        # Loop over the circles and draw them on the frame
        for (x, y, r) in circles:
            cv2.circle(frame, (x, y), r, (0, 255, 0), 2)
            ball_detected = True
            ball_center = (x, y)

    return frame, ball_detected, ball_center


cap = cv2.VideoCapture(0)

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    # Detect the ball in the frame
    frame, ball_detected, ball_center = detect_ball(frame)

    # Display the frame with ball detection
    cv2.imshow("Ball Detection", frame)

    # Exit the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()

