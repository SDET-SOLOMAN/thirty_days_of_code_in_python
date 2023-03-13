from turtle import Turtle

ALIGN = 'center'
FONT = ("Verdana", 30, "normal")


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.left_side = 0
        self.right_side = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 250)

    def left_score(self):
        self.left_side += 1
        self.clear()

    def right_score(self):
        self.right_side += 1
        self.clear()

    def show_score(self):
        self.write(f"{self.left_side} : {self.right_side}", align=ALIGN,
                   font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.color("white")
        self.write(f"GAME OVER", align=ALIGN, font=FONT)
