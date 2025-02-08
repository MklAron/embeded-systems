from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
O = (0, 0, 0)
P = (255, 0, 0)

heart = [
    O, O, O, O, O, O, O, O,
    O, P, P, O, O, P, P, O,
    P, P, P, P, P, P, P, P,
    P, P, P, P, P, P, P, P,
    O, P, P, P, P, P, P, O,
    O, O, P, P, P, P, O, O,
    O, O, O, P, P, O, O, O,
    O, O, O, O, O, O, O, O
]

def red():
    sense.clear(255, 0, 0)

def blue():
    sense.clear(0, 0, 255)

def green():
    sense.clear(0, 255, 0)

def yellow():
    sense.clear(255, 255, 0)
def blinking_red_heart():
    for _ in range(5):
        sense.set_pixels(heart)
        sleep(0.5)
        sense.clear()
        sleep(0.5)
sense.stick.direction_up = blinking_red_heart
sense.stick.direction_down = blue
sense.stick.direction_left = green
sense.stick.direction_right = yellow
sense.stick.direction_middle = sense.clear
while True:
    pass
