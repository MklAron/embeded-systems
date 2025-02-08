from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
P0 = 1013.25
def calculate_altitude(P, P0=1013.25):
    h = 44331 * (1 - (P / P0) ** (1 / 5.2558))
    return h
while True:
    P = sense.get_pressure()
    altitude = calculate_altitude(P, P0)
    print("Predicted Altitude:", round(altitude, 2), " meters")
    sleep(1)
