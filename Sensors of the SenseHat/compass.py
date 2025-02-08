from sense_hat import SenseHat
import math
import time
sense = SenseHat()
xmin, xmax = -50, 50
ymin, ymax = -50, 50

while True:
    magnet = sense.get_compass_raw()
    x = magnet['x']
    y = magnet['y']
    xz = -1 + ((1 - (-1)) / (xmax - xmin)) * (x - xmin)
    yz = -1 + ((1 - (-1)) / (ymax - ymin)) * (y - ymin)
    if xz == 0 and yz < 0:
        deg = 90
    elif xz == 0 and yz > 0:
        deg = 270
    elif yz < 0:
        deg = 360 + math.atan2(yz, xz) * (180 / math.pi)
    else:
        deg = math.atan2(yz, xz) * (180 / math.pi)
    deg = deg % 360
    if deg >= 337.5 or deg < 22.5:
        sense.show_letter('N')
    elif 22.5 <= deg < 67.5:
        sense.show_letter('n') #for NE
    elif 67.5 <= deg < 112.5:
        sense.show_letter('E')
    elif 112.5 <= deg < 157.5:
        sense.show_letter('e') #for SE
    elif 157.5 <= deg < 202.5:
        sense.show_letter('S')
    elif 202.5 <= deg < 247.5:
        sense.show_letter('s') #for SW
    elif 247.5 <= deg < 292.5:
        sense.show_letter('W')
    elif 292.5 <= deg < 337.5:
        sense.show_letter('w') #for NW

    time.sleep(0.2)
