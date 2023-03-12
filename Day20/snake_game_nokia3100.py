import time
from turtle import Screen

from Day20.food_class_inheritance import Food
from Day20.scoreboard_inherence_oop import Score
from Day20.snake_oop import Snake

game_screen = Screen()  # initiate Screen
game_screen.setup(width=600, height=600)  # set screen dimensions
game_screen.bgcolor('black')  # set background color to black
game_screen.title('My Super Nokia 3310 Snake Game')  # set window name
game_screen.tracer(0)  # Turn off animation so each block of snake won't move line by line

nums = 0  # nums is used for X coordinate position of snake pieces
my_snakes = []  # list of future snake pieces

snake = Snake()
food = Food()
score = Score()

game_screen.listen()  # Method to listen our keyboard
game_screen.onkey(snake.up, "Up")
game_screen.onkey(snake.down, "Down")
game_screen.onkey(snake.left, "Left")
game_screen.onkey(snake.right, "Right")

game_is_on = True

while game_is_on:

    game_screen.update()  # Update snake movement with Tracer
    time.sleep(.22)  # adding sleep to make snake gui slower
    snake.move()
    score.show_score()

    if snake.head.distance(food) < 15:
        snake.snake_growth()
        food.refresh()
        score.increase_score()

    if not snake.is_it_wall():
        score.game_over()
        game_is_on = False

    for snakes in snake.my_snakes[1:]:
        if snake.head.distance(snakes) < 10:
            score.game_over()
            game_is_on = False

game_screen.exitonclick()
