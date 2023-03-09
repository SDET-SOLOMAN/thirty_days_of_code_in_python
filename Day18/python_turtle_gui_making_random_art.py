import turtle
from turtle import Screen, Turtle
from random import choice, randint

timmy_the_turtle = Turtle()
turtle.colormode(255)

screen = Screen()
timmy_the_turtle.shape('turtle')
timmy_the_turtle.color('red')
my_color = ['red', 'green', 'pink', 'black', "plum4", "purple", "yellow", "SkyBlue", "SeaGreen", "RoyalBlue4"]
directions = [0, 90, 180, 270]
move = 0
timmy_the_turtle.speed(10)
timmy_the_turtle.pensize(13)


def pick_a_color():
    r = randint(0, 255)
    g = randint(0, 255)
    b = randint(0, 255)
    rand_colors = (r, g, b)
    return rand_colors


def make_a_turn():
    timmy_the_turtle.forward(30)
    return timmy_the_turtle.setheading(choice(directions))


while move < 400:
    timmy_the_turtle.color(pick_a_color())
    make_a_turn()
    move += 1

screen.exitonclick()
