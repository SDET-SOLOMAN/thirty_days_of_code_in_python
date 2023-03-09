import colorgram
import turtle as turtle_module
import random

# Extract 6 colors from an image.
colors = colorgram.extract('color_pics.png', 30)

# color gram.extract returns Color objects, which let you access
# RGB, HSL, and what proportion of the image was that color.

my_list = []
for num in range(30):
    first_color = colors[num]
    my_list.append((first_color.rgb[0], first_color.rgb[1], first_color.rgb[2]))  # e.g. (255, 151, 210)

# RGB and HSL are named tuples, so values can be accessed as properties.
# These all work just as well:

my_colors = [(204, 155, 102), (71, 107, 129), (163, 76, 50), (235, 239, 243), (123, 153, 169), (132, 173, 156),
             (115, 83, 99), (224, 197, 135), (52, 39, 24), (182, 92, 107), (156, 140, 76), (185, 127, 142),
             (80, 115, 112), (23, 38, 50), (82, 165, 132), (211, 101, 75), (31, 73, 86), (232, 166, 162),
             (10, 27, 26), (36, 32, 33), (148, 37, 34), (114, 122, 156), (148, 36, 39), (225, 170, 174),
             (91, 140, 151), (170, 204, 194), (39, 74, 72)]

turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(my_colors))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
