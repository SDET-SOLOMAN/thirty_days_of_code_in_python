from turtle import Screen
from Day21.ball import Ball
from Day21.score import Score
from paddles import Paddle

game_screen = Screen()  # initiate Screen
game_screen.setup(width=800, height=600)  # set screen dimensions
game_screen.bgcolor('black')  # set background color to black
game_screen.title('SDET-SOLOMAN\'S Ping Pong Game')  # set window name
game_screen.tracer(0)  # Turn off animation so each block of snake won't move line by line

my_right_paddle = Paddle((350, 0))
my_right_paddle.create_a_paddle()
my_left_paddle = Paddle((-350, 0))
my_left_paddle.create_a_paddle()

my_ball = Ball()
my_ball.create_the_ball()

game_score = Score()

game_screen.listen()
game_screen.onkey(my_right_paddle.up, "Up")
game_screen.onkey(my_right_paddle.down, "Down")
game_screen.onkey(my_left_paddle.up, "w")
game_screen.onkey(my_left_paddle.down, "s")

is_game_on = True

while is_game_on:

    game_score.show_score()
    game_screen.update()
    my_ball.ball_is_moving()
    sleep_checker = True
    if my_ball.speed <= .003:
        sleep_checker = False

    if my_ball.ycor() >= 290 or my_ball.ycor() <= -290:
        my_ball.bounced_ball()

    if (my_ball.distance(my_right_paddle) < 60 and my_ball.xcor() > 320) or \
            (my_ball.distance(my_left_paddle) < 60 and my_ball.xcor()) < -320:
        my_ball.bounced_paddle()
        if sleep_checker:
            my_ball.speed -= .003

    if my_ball.xcor() > 350:
        game_score.left_score()
        my_ball.create_the_ball()
        if sleep_checker:
            my_ball.speed -= .003


    elif my_ball.xcor() < - 350:
        game_score.right_score()
        my_ball.create_the_ball()
        if sleep_checker:
            my_ball.speed -= .003

    # Detect Wall Collision

game_screen.exitonclick()
