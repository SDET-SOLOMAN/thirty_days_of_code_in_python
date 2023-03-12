from turtle import Turtle, Screen
from random import randint

my_colors = ['red', 'orange', 'pink', 'blue']
list_of_matveevas = []
number = 20
is_Game_On = True

screen = Screen()
screen.setup(width=500, height=500)
user_bet = screen.textinput(title='Make the Bet', prompt="Which of the Matveev Turtle you think is going to win? ")

for num in my_colors:
    matveeva = Turtle('turtle')
    matveeva.color(num)
    matveeva.penup()
    matveeva.goto(x=(-224), y=(-80 + number))
    number += 40
    list_of_matveevas.append(matveeva)


while is_Game_On:
    for turtle in list_of_matveevas:
        my_distance = randint(0, 10)
        turtle.forward(my_distance)
        if turtle.pos()[0] >= 249.00:
            winning_turtle = turtle.pencolor()
            if user_bet == winning_turtle:
                print(f"You have won Juliana with color {winning_turtle} came the first")
            else:
                print(f"better luck next time, YOU LOST {winning_turtle}")
            is_Game_On = False


screen.exitonclick()