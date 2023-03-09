import turtle
from turtle import Screen, Turtle
from random import choice, randint

timmy_the_turtle = Turtle()
turtle.colormode(255)

screen = Screen()
timmy_the_turtle.shape('turtle')
timmy_the_turtle.color('red')

directions = [0, 90, 180, 270]
move = 0
cur_heading = timmy_the_turtle.heading()

timmy_the_turtle.speed(10)
timmy_the_turtle.pensize(4)


def draw_spirograpth(gap_size):
    for num in range(int(360 / gap_size)):
        timmy_the_turtle.color(pick_a_color())
        timmy_the_turtle.circle(100)
        timmy_the_turtle.setheading(timmy_the_turtle.heading() + gap_size)


def pick_a_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rand_colors = (r, g, b)

    return rand_colors


draw_spirograpth(10)

screen.exitonclick()
