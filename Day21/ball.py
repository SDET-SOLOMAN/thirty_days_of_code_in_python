from turtle import Turtle
from time import sleep

SPEED = .13


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.x_move = 10
        self.y_move = 10
        self.speed = .15

    def create_the_ball(self):
        self.setposition(0, 0)
        self.color('red')
        self.penup()
        self.shapesize(1, 1)

    def ball_is_moving(self):
        current_x = self.xcor() + self.x_move
        current_y = self.ycor() + self.y_move
        self.goto(current_x, current_y)
        self.ball_speed()

    def bounced_ball(self):
        self.y_move *= -1

    def bounced_paddle(self):
        self.x_move *= -1

    def ball_speed(self):
        sleep(self.speed)


