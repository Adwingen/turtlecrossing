#player.py

import random
import time
from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.color("black")
        self.shape("turtle")
        self.penup()
        self.go_to_start()
        self.setheading(90)

    def go_up(self):
        self.forward(MOVE_DISTANCE)
        #self.spin_animation()

    def go_down(self):
        if self.ycor() > STARTING_POSITION[1]:
            self.backward(MOVE_DISTANCE)
            #self.spin_animation()

    def spin_animation(self):
        for _ in range(5):
            self.right(18)  # Gira 90 graus no total (5 x 18)
            time.sleep(0.01)

    def go_to_start(self):
        self.goto(STARTING_POSITION)

    def is_at_finnish_line(self):
        if self.ycor() > FINISH_LINE_Y:
            return  True
        else:
            return False

