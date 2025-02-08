import cv2
from pyzbar import pyzbar
import os
import sys

sys.stderr = open(os.devnull, 'w')

def process_image(image):
    barcodes = pyzbar.decode(image)
    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
        barcode_data = barcode.data.decode("utf-8")
        barcode_type = barcode.type
        text = f"{barcode_data} ({barcode_type})"
        cv2.putText(image, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
    return image

cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break
    cv2.imshow("Nyomj 's'-t a feldolgozáshoz", frame)
    key = cv2.waitKey(1) & 0xFF
    if key == ord('s'):
        processed_image = process_image(frame)
        cv2.imshow("Feldolgozott kép", processed_image)
        cv2.waitKey(0)
        break
    elif key == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
