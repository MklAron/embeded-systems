from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
O = (0, 0, 0) 
R = (255, 0, 0)
right_arrow = [
    O, O, O, O, O, O, O, O,
    O, O, O, R, O, O, O, O,
    O, O, O, O, R, O, O, O,
    O, R, R, R, R, R, O, O,
    O, O, O, O, R, O, O, O,
    O, O, O, R, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O
]

up_arrow = [
    O, O, O, O, O, O, O, O,
    O, O, O, R, O, O, O, O,
    O, O, R, R, R, O, O, O,
    O, R, O, R, O, R, O, O,
    O, O, O, R, O, O, O, O,
    O, O, O, R, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O
]

down_arrow = [
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, R, O, O, O, O,
    O, O, O, R, O, O, O, O,
    O, R, O, R, O, R, O, O,
    O, O, R, R, R, O, O, O,
    O, O, O, R, O, O, O, O,
    O, O, O, O, O, O, O, O
]

left_arrow = [
    O, O, O, O, O, O, O, O,
    O, O, O, R, O, O, O, O,
    O, O, R, O, O, O, O, O,
    O, R, R, R, R, R, O, O,
    O, O, R, O, O, O, O, O,
    O, O, O, R, O, O, O, O,
    O, O, O, O, O, O, O, O,
    O, O, O, O, O, O, O, O
]
while True:
    # go through all joystick events
    for event in sense.stick.get_events():
        # Check if the joystick was pressed
        if event.action == "pressed":
            # Check which direction
            if event.direction == "up":
                sense.set_pixels(up_arrow)  # Display up arrow
            elif event.direction == "down":
                sense.set_pixels(down_arrow)  # Display down arrow
            elif event.direction == "left":
                sense.set_pixels(left_arrow)  # Display left arrow
            elif event.direction == "right":
                sense.set_pixels(right_arrow)  # Display right arrow
            elif event.direction == "middle":
                sense.show_letter("M")  # Show "M" for middle (enter key)

            # Wait a while and then clear the screen
            sleep(0.5)
            sense.clear()
