from turtle import Turtle

ALIGN = 'center'
FONT = ("Verdana", 15, "normal")


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.current_score = 0
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 275)

    def increase_score(self):
        self.current_score += 1
        self.clear()
        self.show_score()

    def show_score(self):
        self.write(f"Score is {self.current_score}", align=ALIGN,
                   font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align=ALIGN, font=FONT)