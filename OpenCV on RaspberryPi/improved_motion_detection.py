from imutils.video import VideoStream
import datetime
import imutils
import time
import cv2

# Constants
T = 50  # Threshold for binary image
min_area = 1000  # Minimum area for motion detection
background = None  # For storing the weighted average background
video_path = None  # Path to the video file (set to None for live stream)

# Initialize video stream or file
if video_path is None:
    vs = VideoStream().start()
    time.sleep(2)  # Warm up the camera
else:
    vs = cv2.VideoCapture(video_path)

# Process frames
while True:
    frame = vs.read()
    frame = frame if video_path is None else frame[1]
    state = "No change"  # Initial state for motion detection

    if frame is None:  # Break if no frame
        break

    # Preprocessing
    frame = imutils.resize(frame, width=500)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.GaussianBlur(gray, (21, 21), 0)

    # Initialize the background as a float array
    if background is None:
        background = gray.copy().astype("float")
        continue

    # Calculate delta frame (difference between current and background)
    delta_frame = cv2.absdiff(gray, cv2.convertScaleAbs(background))

    # Apply thresholding and dilation
    threshold = cv2.threshold(delta_frame, T, 255, cv2.THRESH_BINARY)[1]
    threshold = cv2.dilate(threshold, None, iterations=2)

    # Detect contours
    cnts = cv2.findContours(threshold.copy(), cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    cnts = imutils.grab_contours(cnts)

    for c in cnts:
        if cv2.contourArea(c) < min_area:
            continue

        # Draw bounding box and update state
        (x, y, w, h) = cv2.boundingRect(c)
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)
        state = "New object"

    # Update the background using a weighted average
    cv2.accumulateWeighted(gray, background, 0.5)

    # Display the state and timestamp on the frame
    cv2.putText(frame, "Room Status: {}".format(state), (10, 20),
                cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 2)
    cv2.putText(frame, datetime.datetime.now().strftime("%A %d %B %Y %I:%M:%S%p"),
                (10, frame.shape[0] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.35, (0, 0, 255), 1)

    # Show the processed frames
    cv2.imshow("Camera image", frame)
    cv2.imshow("Threshold", threshold)
    cv2.imshow("Delta frame", delta_frame)

    # Exit on pressing 'q'
    key = cv2.waitKey(1) & 0xFF
    if key == ord("q"):
        break

# Cleanup
vs.stop() if video_path is None else vs.release()
cv2.destroyAllWindows()
