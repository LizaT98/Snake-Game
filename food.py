from turtle import Turtle, Screen
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.penup()
        self.shapesize(stretch_len = 0.7, stretch_wid = 0.7)
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        x_coordinate = random.randint(-230, 230)
        y_coordinate = random.randint(-175, 175)
        self.goto(x_coordinate, y_coordinate)
