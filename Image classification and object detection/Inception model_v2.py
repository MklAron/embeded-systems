import numpy as np
import time
import cv2

# Paths to your files
image_path = "image.jpg"
label_path = "imagenet1000_labels.txt"
prototxt_path = "googlenet.prototxt"
model_path = "googlenet.caffemodel"

# Load the image
image = cv2.imread(image_path)
if image is None:
    raise FileNotFoundError(f"Could not load image at path: {image_path}")

# Read the labels
rows = open(label_path).read().strip().split("\n")
classes = [r.split(",")[0] for r in rows]

# Prepare the image as a blob
blob = cv2.dnn.blobFromImage(image, 1, (224, 224), (104, 117, 123))

# Load the model
print("Loading model...")
net = cv2.dnn.readNetFromCaffe(prototxt_path, model_path)

# Perform inference
net.setInput(blob)
start = time.time()
preds = net.forward()
end = time.time()
print("Classification time: {:.5} seconds".format(end - start))
idxs = np.argsort(preds[0])[::-1][:5]

# Display the top prediction on the image
for (i, idx) in enumerate(idxs):
    label = classes[idx]
    prob = preds[0][idx] * 100
    print(f"{i + 1}. label: {label}, probability: {prob:.2f}%")
    
    if i == 0:
        text = f"Label: {label}, {prob:.2f}%"
        cv2.putText(image, text, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.4, (0, 0, 255), 2)

cv2.imshow("Classification Result", image)
cv2.waitKey(0) 
cv2.destroyAllWindows()