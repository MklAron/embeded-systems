import cv2
import imutils
import numpy as np
from imutils.video import VideoStream
import time

# Constants
video_path = None
buffsize = 64
indx = 0

# Lower and upper boundaries of a "green" object in HSV color space
green_range = [(25, 55, 5), (65, 255, 255)]

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

    # Create a binary mask
    mask = cv2.inRange(hsv, green_range[0], green_range[1])
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

        # Update the path list1
        if indx < buffsize:
            path[indx] = (center[0], center[1])
            indx += 1
        else:
            path[0:indx-1] = path[1:indx]
            path[indx-1] = (center[0], center[1])

    # Draw the movement track
    for i in range(1, len(path)):
        if path[i - 1] is None or path[i] is None:
            continue

        # Compute thickness of the line based on position in the path
        thickness = int(np.sqrt(len(path) / float(i + 1)) * 2.5)
        cv2.line(frame, (path[i-1][0], path[i-1][1]), (path[i][0], path[i][1]), (0, 0, 255), thickness)

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
