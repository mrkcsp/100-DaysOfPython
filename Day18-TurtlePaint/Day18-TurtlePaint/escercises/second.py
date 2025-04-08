from turtle import Screen
import turtle as t

timmy = t.Turtle()

def trat():
    for _ in range(25):
        timmy.forward(8)
        timmy.penup()
        timmy.forward(4)
        timmy.pendown()


trat()
timmy.left(90)
trat()
timmy.left(90)
trat()
timmy.left(90)
trat()




screen = Screen()
screen.exitonclick()