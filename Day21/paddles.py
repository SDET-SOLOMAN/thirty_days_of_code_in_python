from turtle import Turtle

MOVE_DISTANCE = 20


class Paddle(Turtle):
    def __init__(self, position_from_user):
        super().__init__()
        self.shape('square')
        self.setposition(position_from_user)

    def create_a_paddle(self):
        self.color('white')
        self.penup()
        self.shapesize(5, 1)

    def up(self):
        new_position = self.ycor() + 20
        self.goto(self.xcor(), new_position)

    def down(self):
        new_position = self.ycor() - 20
        self.goto(self.xcor(), new_position)
