from turtle import Screen
import turtle as t
import random

timmy = t.Turtle()

def shape(angles, dimension):
    for _ in range(angles):
        timmy.forward(dimension)
        grades = 360 / angles
        timmy.left(grades)



shape(3, 100)
shape(4, 100)
shape(5, 100)
shape(6, 100)
shape(7, 100)
shape(8, 100)
shape(9, 100)
shape(10, 100)









screen = Screen()
screen.exitonclick()