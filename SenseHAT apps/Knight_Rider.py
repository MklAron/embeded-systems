from sense_hat import SenseHat
import time
sense = SenseHat()
p = [2, 3]
light_len = 3
space_size = 8
speed = 1 / 7

r = (255, 0, 0)
n = (0, 0, 0)
space = [
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    r, r, r, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n,
    n, n, n, n, n, n, n, n
]
def shift_right():
    global p
    if p[0] < space_size - 1:
        p[0] += 1
        sense.clear()
        for i in range(light_len):
            sense.set_pixel(p[1], p[0] - i, r)

def shift_left():
    global p
    if p[0] > light_len - 1:
        p[0] -= 1
    
        sense.clear()
        for i in range(light_len):
            sense.set_pixel(p[1], p[0] - i, r)

def main():
    global p
    while True:
        while True:
            shift_right()
            time.sleep(speed)
            if p[0] == space_size - 1:
                break

        while True:
            shift_left()
            time.sleep(speed)
            if p[0] == light_len - 1:
                break

main()
