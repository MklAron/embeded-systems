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
sense.set_pixels(heart)
sleep(3)
sense.clear()
