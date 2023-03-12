from turtle import Turtle
from random import randint

x = randint(-280, 280)
y = randint(-280, 280)


class Food(Turtle):
    """Created Food Sub-Class from Super Class Turtle"""

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(.5, .5)
        self.color('red')
        self.refresh()

    def refresh(self):
        x = randint(-280, 280)
        y = randint(-280, 280)
        self.goto(x, y)
