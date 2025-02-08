import cv2
from pyzbar import pyzbar
import os
import sys

sys.stderr = open(os.devnull, 'w')

def process_frame(frame):
    barcodes = pyzbar.decode(frame)
    for barcode in barcodes:
        (x, y, w, h) = barcode.rect
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        barcode_data = barcode.data.decode("utf-8")
        barcode_type = barcode.type

        text = f"{barcode_data} ({barcode_type})"
        cv2.putText(frame, text, (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    return frame

cap = cv2.VideoCapture(0)

print("Nyomd meg a 'q'-t a kilepeshez.")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    processed_frame = process_frame(frame)

    cv2.imshow("Vonalkod/QR-kod Olvaso", processed_frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Erőforrások felszabadítása
cap.release()
cv2.destroyAllWindows()
