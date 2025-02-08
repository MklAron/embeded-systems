import numpy as np
import cv2

# Paths to model files
prototxt_path = "ora10//MobileNetSSD_deploy_prototxt.txt"
model_path = "ora10//MobileNetSSD_deploy.caffemodel"

# Confidence threshold
conf_limit = 0.25

# Class labels and random colors
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog",
           "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train",
           "tv/monitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

# Load the model
print("Loading model...")
net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)

# Open a video stream (0 for webcam, or replace with video file path)
print("Starting video stream...")
video_stream = cv2.VideoCapture(0)  # Use "path/to/video.mp4" for a video file

while True:
    # Capture frame-by-frame
    ret, frame = video_stream.read()
    if not ret:
        print("No frame captured. Exiting...")
        break

    # Get frame dimensions and preprocess for the model
    (h, w) = frame.shape[:2]
    blob = cv2.dnn.blobFromImage(cv2.resize(frame, (300, 300)), 0.007843,
                                 (300, 300), 127.5)

    # Set the blob as input and perform a forward pass
    net.setInput(blob)
    detections = net.forward()

    # Loop through detections
    for i in np.arange(0, detections.shape[2]):
        confidence = detections[0, 0, i, 2]
        if confidence > conf_limit:
            idx = int(detections[0, 0, i, 1])
            box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])
            (startX, startY, endX, endY) = box.astype("int")

            label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
            print(label)

            # Draw bounding box and label on the frame
            cv2.rectangle(frame, (startX, startY), (endX, endY), COLORS[idx], 2)
            y = startY - 15 if startY - 15 > 15 else startY + 15
            cv2.putText(frame, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)

    # Show the frame
    cv2.imshow("Real-Time Object Detection", frame)

    # Break on 'q' key press
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release the video stream and close all OpenCV windows
video_stream.release()
cv2.destroyAllWindows()
