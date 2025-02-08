import cv2
import imutils
import numpy as np
from imutils.video import VideoStream
import time

# Constants
video_path = None
buffsize = 64
indx = 0

# Lower and upper boundaries of a "red" object in HSV color space
red_ranges = [
    (0, 120, 70), (10, 255, 255),  # Low Red
    (170, 120, 70), (180, 255, 255)  # High Red
]

# Initialize the list of tracked points
path = np.zeros((buffsize, 2), dtype='int')

# Initialize video stream
if video_path is None:
    vs = VideoStream().start()
    time.sleep(2)  # Allow camera to warm up
else:
    vs = cv2.VideoCapture(video_path)

while True:
    # Read the current frame
    frame = vs.read()
    frame = frame if video_path is None else frame[1]

    if frame is None:  # Break if no frame is available
        break

    # Resize, blur, and convert the frame to HSV color space
    frame = imutils.resize(frame, width=500)
    blur = cv2.GaussianBlur(frame, (9, 9), 0)
    hsv = cv2.cvtColor(blur, cv2.COLOR_BGR2HSV)

    # Create masks for red color using the defined ranges
    mask_low_red = cv2.inRange(hsv, red_ranges[0], red_ranges[1])
    mask_high_red = cv2.inRange(hsv, red_ranges[2], red_ranges[3])

    # Combine the two masks to cover the full red range
    mask = cv2.bitwise_or(mask_low_red, mask_high_red)

    # Perform morphological operations to reduce noise
    mask = cv2.erode(mask, None, iterations=2)
    mask = cv2.dilate(mask, None, iterations=2)

    # Find contours in the mask
    cnts = cv2.findContours(mask.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    center = None  # Variable to store the center of the detected object

    if len(cnts) > 0:
        # Find the largest contour
        cnt = max(cnts, key=cv2.contourArea)

        # Compute the minimum enclosing circle and centroid
        ((x, y), radius) = cv2.minEnclosingCircle(cnt)
        M = cv2.moments(cnt)
        center = (int(M["m10"] / M["m00"]), int(M["m01"] / M["m00"]))

        # Draw the circle and centroid if the radius is above a threshold
        if radius > 10:
            cv2.circle(frame, (int(x), int(y)), int(radius), (0, 255, 255), 2)
            cv2.circle(frame, center, 5, (0, 0, 255), -1)

        # Update the path list
        if indx < buffsize:
            path[indx] = (center[0], center[1])
            indx += 1
        else:
            path[0:indx-1] = path[1:indx]
            path[indx-1] = (center[0], center[1])
    else:
        # If no contours are found, clear the path and reset the index
        path[:] = 0
        indx = 0

    # Draw the movement track with reversed thickness
    for i in range(1, indx):
        if path[i - 1] is None or path[i] is None:
            continue

        # Compute thickness (thicker closer to the center of the object)
        thickness = int((float(i) / indx) * 10 + 2)  # Scale thickness from 2 to 10
        cv2.line(frame, (path[i-1][0], path[i-1][1]), (path[i][0], path[i][1]), (0, 255, 0), thickness)

    # Display the result
    cv2.imshow("Frame", frame)
    cv2.imshow("Mask", mask)

    # Exit on pressing 'q'
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# Cleanup
vs.stop() if video_path is None else vs.release()
cv2.destroyAllWindows()
