from sense_hat import SenseHat
from time import sleep
import random
sense = SenseHat()
background = (0, 0, 0)
snake_color = (0, 255, 0)
food_color = (255, 0, 0)

snake = [(3, 3)]
direction = (0, 1)
food = None
score = 0

def update_display():
    sense.clear()
    for segment in snake:
        sense.set_pixel(segment[1], segment[0], snake_color)
    if food:
        sense.set_pixel(food[1], food[0], food_color)

def place_food():
    while True:
        new_food = (random.randint(0, 7), random.randint(0, 7))
        if new_food not in snake:
            return new_food

def joystick_moved(event):
    global direction
    if event.action == 'pressed':
        if event.direction == 'up' and direction != (1, 0):
            direction = (-1, 0)
        elif event.direction == 'down' and direction != (-1, 0):
            direction = (1, 0)
        elif event.direction == 'left' and direction != (0, 1):
            direction = (0, -1)
        elif event.direction == 'right' and direction != (0, -1):
            direction = (0, 1)

sense.stick.direction_up = joystick_moved
sense.stick.direction_down = joystick_moved
sense.stick.direction_left = joystick_moved
sense.stick.direction_right = joystick_moved

def main():
    global food, score
    food = place_food()
    update_display()
    
    while True:
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])
        if (new_head[0] < 0 or new_head[0] > 7 or
            new_head[1] < 0 or new_head[1] > 7 or
            new_head in snake):
            break
        snake.insert(0, new_head)
        if new_head == food:
            score += 1
            food = place_food()
        else:
            snake.pop()
        
        update_display()
        sleep(0.5)
    sense.show_message("Game Over!", scroll_speed=0.05, text_colour=snake_color)
    sense.show_message('Score: ' + str(score), scroll_speed=0.05, back_colour=w)
    sense.clear()

main()
