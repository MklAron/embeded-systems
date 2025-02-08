import numpy as np
import cv2

# Paths to files
prototxt_path = "MobileNetSSD_deploy_prototxt.txt"
model_path = "MobileNetSSD_deploy.caffemodel"
image_path = "cow.jpg"

# Confidence threshold
conf_limit = 0.25

# Define class labels and random colors for bounding boxes
CLASSES = ["background", "aeroplane", "bicycle", "bird", "boat",
           "bottle", "bus", "car", "cat", "chair", "cow", "diningtable", "dog",
           "horse", "motorbike", "person", "pottedplant", "sheep", "sofa", "train",
           "tv/monitor"]
COLORS = np.random.uniform(0, 255, size=(len(CLASSES), 3))

# Load the pre-trained model
print("Loading model...")
net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)

# Load the input image
image = cv2.imread(image_path)
if image is None:
    raise FileNotFoundError(f"Could not load image at path: {image_path}")

(h, w) = image.shape[:2]

# Preprocess the image into a blob
blob = cv2.dnn.blobFromImage(cv2.resize(image, (300, 300)), 0.007843, (300, 300), 127.5)

# Pass the blob through the network
print("Sending image through the network...")
net.setInput(blob)
detections = net.forward()

# Process detections
for i in np.arange(0, detections.shape[2]):
    # Extract confidence of detection
    confidence = detections[0, 0, i, 2]
    if confidence > conf_limit:
        idx = int(detections[0, 0, i, 1])  # Class index
        box = detections[0, 0, i, 3:7] * np.array([w, h, w, h])  # Bounding box coordinates
        (startX, startY, endX, endY) = box.astype("int")
        label = "{}: {:.2f}%".format(CLASSES[idx], confidence * 100)
        print(label)
        cv2.rectangle(image, (startX, startY), (endX, endY), COLORS[idx], 2)
        y = startY - 15 if startY - 15 > 15 else startY + 15
        cv2.putText(image, label, (startX, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, COLORS[idx], 2)
cv2.imshow("Object Detection", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
