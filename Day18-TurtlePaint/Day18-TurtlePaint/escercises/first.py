from turtle import Turtle, Screen

timmy_the_turtle = Turtle()

timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("red")

timmy_the_turtle.forward(50)

for _ in range(3):
    timmy_the_turtle.left(90)
    timmy_the_turtle.forward(50)

timmy_the_turtle.forward(100)

for _ in range(3):
    timmy_the_turtle.left(90)
    timmy_the_turtle.forward(100)

timmy_the_turtle.forward(150)

for _ in range(3):
    timmy_the_turtle.left(90)
    timmy_the_turtle.forward(150)
    
timmy_the_turtle.forward(200)

for _ in range(3):
    timmy_the_turtle.left(90)
    timmy_the_turtle.forward(200)

timmy_the_turtle.forward(250)

for _ in range(3):
    timmy_the_turtle.left(90)
    timmy_the_turtle.forward(250)
    
timmy_the_turtle.forward(300)

for _ in range(3):
    timmy_the_turtle.left(90)
    timmy_the_turtle.forward(300)

screen = Screen()
screen.exitonclick()