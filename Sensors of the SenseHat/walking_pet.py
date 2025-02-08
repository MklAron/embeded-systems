from sense_hat import SenseHat
from time import sleep
import math
sense = SenseHat()
threshold = 1.5
BLACK = (0, 0, 0)
GREEN = (8, 138, 15)
PURPLE = (248, 3, 252)
YELLOW = (244, 252, 3)
cat_pattern1 = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 2, 0, 2, 0],
    [0, 2, 1, 1, 2, 3, 3, 0],
    [0, 1, 1, 1, 3, 0, 3, 1],
    [0, 1, 1, 1, 1, 3, 3, 0],
    [0, 1, 0, 1, 0, 1, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]

cat_pattern2 = [
    [0, 0, 0, 0, 0, 0, 0, 0],
    [2, 0, 0, 0, 0, 0, 0, 0],
    [0, 2, 0, 0, 2, 0, 2, 0],
    [0, 2, 1, 1, 2, 3, 3, 0],
    [0, 1, 1, 1, 3, 0, 3, 1],
    [0, 1, 1, 1, 1, 3, 3, 0],
    [0, 0, 1, 0, 1, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0]
]
def convert_pattern_to_pixels(pattern):
    pixels = []
    for row in pattern:
        for pixel in row:
            if pixel == 0:
                pixels.append(BLACK)
            elif pixel == 1:
                pixels.append(GREEN)
            elif pixel == 2:
                pixels.append(PURPLE)
            elif pixel == 3:
                pixels.append(YELLOW)
    return pixels
def animate_walking_cat():
    for _ in range(5):
        sense.set_pixels(convert_pattern_to_pixels(cat_pattern1))
        sleep(0.5)
        sense.set_pixels(convert_pattern_to_pixels(cat_pattern2))
        sleep(0.5)
    sense.clear()
def calculate_force(acceleration):
    x = acceleration['x']
    y = acceleration['y']
    z = acceleration['z']
    force = math.sqrt(x**2 + y**2 + z**2)
    return force
while True:
    acceleration = sense.get_accelerometer_raw()
    force = calculate_force(acceleration)
    if force > threshold:
        animate_walking_cat()
    sleep(0.1)
