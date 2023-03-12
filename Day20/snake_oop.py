from turtle import Turtle

MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
POSITIONS = [(0, 0), (-10, 0), (-20, 0)]


class Snake:
    def __init__(self):
        self.nums = 0  # nums is used for X coordinate position of snake pieces
        self.my_snakes = []  # list of future snake pieces
        self.create_a_snake()
        self.head = self.my_snakes[0]  # setting variable to call out head of snake

    def create_a_snake(self):
        # Snake for loop to create initial Snake pieces
        for num in POSITIONS:
            self.add_piece(num)

    # adds one snake per call
    def add_piece(self, position):
        my_snake = Turtle("square")  # set snake shape to Square
        my_snake.color("white")  # set snake color to white
        my_snake.penup()  # lift pen up so no drawing when moving snake in XY coordinates
        my_snake.goto(position)  # position of the snake
        self.nums -= 20  # -20 in X coordinate each time to add pieces of snake to the left
        self.my_snakes.append(my_snake)  # adding to the list of snake pieces

    # Adds snake to the end of the list
    def snake_growth(self):
        self.add_piece(self.my_snakes[-1].position())

    def move(self):
        # Last snake changes XY position to the XY position of the snake in front of it,
        # and they all follow the first/head
        for snake in range(len(self.my_snakes) - 1, 0, -1):
            new_position = self.my_snakes[snake - 1].pos()
            self.my_snakes[snake].goto(new_position)
        self.head.forward(MOVE_DISTANCE)

    # According to the rules of SNAKE GAME, if Snake is going up, it cant go down
    # if snake is going down, it can't go up, if its left, it can't turn right,
    # Therefore, we have if conditional logic:
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # Checks if there is a wall, returns a bool value
    def is_it_wall(self):
        if self.head.xcor() > 280 or self.head.xcor() < - 280 or self.head.ycor() > 280 or self.head.ycor() < - 280:
            return False
        return True
