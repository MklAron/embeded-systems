from sense_hat import SenseHat
import time
sense = SenseHat()
state = 0
w = (255, 255, 255)
r = (255, 0, 0)
g = (0, 255, 0)
y = (255, 255, 0)
n = (0, 0, 0)

patterns = {
    "red": [
        n, n, n, r, r, n, n, n,
        n, n, n, r, r, n, n, n,
        n, n, n, n, n, n, n, n,
        n, n, n, n, n, n, n, n,
        n, n, n, n, n, n, n, n,
        n, n, n, n, n, n, n, n,
        n, n, n, n, n, n, n, n,
        n, n, n, n, n, n, n, n
    ],
    "red_yellow": [
        n, n, n, r, r, n, n, n,
        n, n, n, r, r, n, n, n,
        n, n, n, n, n, n, n, n,
        n, n, n, y, y, n, n, n,
        n, n, n, y, y, n, n, n,
        n, n, n, n, n, n, n, n,
        n, n, n, n, n, n, n, n,
        n, n, n, n, n, n, n, n
    ],
    "yellow": [
        n, n, n, n, n, n, n, n,
        n, n, n, n, n, n, n, n,
        n, n, n, n, n, n, n, n,
        n, n, n, y, y, n, n, n,
        n, n, n, y, y, n, n, n,
        n, n, n, n, n, n, n, n,
        n, n, n, n, n, n, n, n,
        n, n, n, n, n, n, n, n
    ],
    "green": [
        n, n, n, n, n, n, n, n,
        n, n, n, n, n, n, n, n,
        n, n, n, n, n, n, n, n,
        n, n, n, n, n, n, n, n,
        n, n, n, n, n, n, n, n,
        n, n, n, n, n, n, n, n,
        n, n, n, g, g, n, n, n,
        n, n, n, g, g, n, n, n
    ]
}

def traffic_light_state(pattern_key, duration=1):
    sense.set_pixels(patterns[pattern_key])
    time.sleep(duration)
    sense.clear()

def out_of_order_state():
    sense.set_pixels(patterns["yellow"])
    time.sleep(0.5)
    sense.clear()
    time.sleep(0.5)
def set_state():
    global state
    if state < 3:
        state += 1
    elif state == 3:
        state = 0
def button_event(event):
    global state
    if event.action == 'released':
        if state != 4:
            state = 4
        else:
            state = 3
sense.stick.direction_middle = button_event
def main():
    global state
    while True:
        if state == 0:
            traffic_light_state("red", 3)
        elif state == 1:
            traffic_light_state("red_yellow", 1)
        elif state == 2:
            traffic_light_state("green", 2)
        elif state == 3:
            traffic_light_state("yellow", 1)
        else:
            out_of_order_state()
        set_state()
main()
