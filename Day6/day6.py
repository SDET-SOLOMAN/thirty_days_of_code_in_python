# Reebor's World Challenges

# The Game is in following website:

# https://reeborg.ca/reeborg.html?lang=en&mode=python&menu=worlds%2Fmenus%2Freeborg_intro_en.json&name=Hurdle%201&url=worlds%2Ftutorial_en%2Fhurdle1.json

# 1 Hurdles race

# More advanced

# You may have noticed that your solution has some repeated patterns.
# If you know how to define functions, define a function named jump() and use it to simplify your program.

# Difficulty level 2/10


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    move()
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()


for num in range(0, 6):
    jump()


# 2 Hurdles race

# Reeborg has entered a hurdle race, but he does not know in advance how long the race is.
# Make him run the course, following
# a path similar to the one shown, but stopping at the only flag that will be shown after the race has started.
# What you need to know

# The functions move() and turn_left().
# The condition at_goal() and its negation.
# How to use a while loop.
# Your program should also be valid for world Hurdles 1.

# Difficulty level 3/ 10

while not at_goal():
    jump()


# 3 What you need to know

# The functions move() and turn_left().
# The conditions front_is_clear() or wall_in_front(), at_goal(), and their negation.
# How to use a while loop and an if statement.
# Your program should also be valid for worlds Hurdles 1 and Hurdles 2.
# Difficulty level 4 /10

def jump():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

while not at_goal():
    if front_is_clear():
        move()
    elif wall_in_front():
       jump()

# 4 Reeborg has entered a hurdle race. Make him run the course, following the path shown.

# The position, the height and the number of hurdles changes each time this world is reloaded.
# What you need to know
# You should be able to write programs that are valid for worlds Around 4 and Hurdles 3,
# and ot combine them for this last hurdles race.
# Your program should also be valid for worlds Hurdles 1, Hurdles 2 et Hurdles 3
# Difficulty level 5 /10

def turn_right():
    turn_left()
    turn_left()
    turn_left()


def jump():
    while wall_on_right() and front_is_clear():
        move()
    if front_is_clear() or right_is_clear():
        turn_right()
        move()
        turn_right()


while not at_goal():
    if front_is_clear() and wall_on_right():
        move()
    elif wall_in_front() and wall_on_right():
        turn_left()
        jump()
    elif not at_goal():
        move()

# 5 What you need to know

# The functions move() and turn_left().
# Either the test front_is_clear() or wall_in_front(), right_is_clear() or wall_on_right(), and at_goal().
# How to use a while loop and if/elif/else statements.
# It might be useful to know how to use the negation of a test (not in Python).

def turn_right():
    turn_left()
    turn_left()
    turn_left()


while not at_goal():
    while front_is_clear():
        if not at_goal():
            move()
    if at_goal():
        break
    elif wall_on_right() and front_is_clear():
        move()
    elif wall_in_front() and right_is_clear():
        turn_right()
        move()
    elif wall_in_front() and wall_on_right():
        turn_left()
    elif front_is_clear() and right_is_clear():
        turn_right()
        move()