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

def number_gen(event):
    if event.action == "pressed":
        val = random.randint(1, 6)
        print(val)
        if val == 1:
            sense.set_pixels(one_img)
        elif val == 2:
            sense.set_pixels(two_img)
        elif val == 3:
            sense.set_pixels(three_img)
        elif val == 4:
            sense.set_pixels(four_img)
        elif val == 5:
            sense.set_pixels(five_img)
        elif val == 6:
            sense.set_pixels(six_img)
        sleep(2)
        sense.clear()
sense.stick.direction_middle = number_gen
while True:
    pass
