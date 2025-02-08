import cv2
import pytesseract
import numpy as np

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

image_path = "input_image.jpg"
image = cv2.imread(image_path)

height, width = image.shape[:2]
new_width = 640
new_height = int((new_width / width) * height)
resized_image = cv2.resize(image, (new_width, new_height))

gray_image = cv2.cvtColor(resized_image, cv2.COLOR_BGR2GRAY)

gray_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
_, thresholded_image = cv2.threshold(gray_image, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)

custom_config = r'--oem 3 --psm 6'
data = pytesseract.image_to_data(thresholded_image, config=custom_config, output_type=pytesseract.Output.DICT)

for i in range(len(data['text'])):
    if int(data['conf'][i]) > 0:
        x, y, w, h = data['left'][i], data['top'][i], data['width'][i], data['height'][i]
        text = data['text'][i]

        roi = resized_image[y:y+h, x:x+w]


        recognized_text = pytesseract.image_to_string(roi, config=custom_config)

        if recognized_text.strip():

            cv2.rectangle(resized_image, (x, y), (x + w, y + h), (0, 0, 255), 2)
            cv2.putText(resized_image, recognized_text.strip(), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1)


cv2.imshow("Detected Text", resized_image)
cv2.imwrite("output_image.jpg", resized_image)
cv2.waitKey(0)
cv2.destroyAllWindows()
