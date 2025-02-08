from sense_hat import SenseHat
from time import sleep
import random
sense = SenseHat()
o = (0, 0, 0)
b = (0, 0, 255)

one_img = [
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, b, b, o, o, o,
    o, o, o, b, b, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o
]

two_img = [
    o, o, o, o, o, o, o, o,
    o, o, o, b, b, o, o, o,
    o, o, o, b, b, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, o, o, b, b, o, o, o,
    o, o, o, b, b, o, o, o,
    o, o, o, o, o, o, o, o
]

three_img = [
    o, o, o, o, o, o, b, b,
    o, o, o, o, o, o, b, b,
    o, o, o, o, o, o, o, o,
    o, o, o, b, b, o, o, o,
    o, o, o, b, b, o, o, o,
    o, o, o, o, o, o, o, o,
    b, b, o, o, o, o, o, o,
    b, b, o, o, o, o, o, o
]

four_img = [
    o, o, o, o, o, o, o, o,
    o, b, b, o, o, b, b, o,
    o, b, b, o, o, b, b, o,
    o, o, o, o, o, o, o, o,
    o, o, o, o, o, o, o, o,
    o, b, b, o, o, b, b, o,
    o, b, b, o, o, b, b, o,
    o, o, o, o, o, o, o, o
]

five_img = [
    o, o, o, o, o, o, o, o,
    b, b, o, o, o, o, b, b,
    b, b, o, o, o, o, b, b,
    o, o, o, b, b, o, o, o,
    o, o, o, b, b, o, o, o,
    b, b, o, o, o, o, b, b,
    b, b, o, o, o, o, b, b,
    o, o, o, o, o, o, o, o
]

six_img = [
    o, b, b, o, o, b, b, o,
    o, b, b, o, o, b, b, o,
    o, o, o, o, o, o, o, o,
    o, b, b, o, o, b, b, o,
    o, b, b, o, o, b, b, o,
    o, o, o, o, o, o, o, o,
    o, b, b, o, o, b, b, o,
    o, b, b, o, o, b, b, o
]
dice_images = [one_img, two_img, three_img, four_img, five_img, six_img]
def number_gen(event):
    if event.action == "pressed":
        for _ in range(30):
            val = random.randint(1, 6)
            sense.set_pixels(dice_images[val-1])
            sleep(0.1)
        final_val = random.randint(1, 6)
        sense.set_pixels(dice_images[final_val-1])
        sleep(2)
        sense.clear()
sense.stick.direction_middle = number_gen
while True:
    pass
