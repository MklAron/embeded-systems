from sense_hat import SenseHat
import time
import random
sense = SenseHat()
blue = (0, 0, 255)
black = (0, 0, 0)
def shift_down():
    pixels = sense.get_pixels()
    for row in range(7, 0, -1):
        for col in range(8):
            pixels[row * 8 + col] = pixels[(row - 1) * 8 + col]
    for col in range(8):
        pixels[col] = black
    sense.set_pixels(pixels)
def rain_effect():
    while True:
        random_column = random.randint(0, 7)
        sense.set_pixel(random_column, 0, blue)
        time.sleep(0.5)
        shift_down()
rain_effect()
