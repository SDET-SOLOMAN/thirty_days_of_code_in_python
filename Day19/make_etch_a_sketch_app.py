from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()
screen.register_shape('snk.gif')
tim.shape('turtle')
tim.color('red')
print(tim.pos()[0])


def mv_forward():
    tim.forward(10)


def mv_back():
    tim.backward(10)


def mv_clock():
    current_location = tim.heading() + 10
    tim.setheading(current_location)


def mv_anti_clock():
    current_location = tim.heading() - 10
    tim.setheading(current_location)


def clear_and_return():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


screen.listen()
screen.onkey(key='w', fun=mv_forward)
screen.onkey(key='s', fun=mv_back)
screen.onkey(key='d', fun=mv_clock)
screen.onkey(key='a', fun=mv_anti_clock)
screen.onkey(key='c', fun=clear_and_return)

screen.exitonclick()
