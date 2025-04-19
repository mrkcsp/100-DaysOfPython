from turtle import Screen, Turtle
import time
from paddle import Paddle
from ball import Ball

from scoreboard import Scoreboard

screen = Screen()

screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)


right_paddle = Paddle((350, 0))
left_paddle = Paddle((-350, 0))
ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")




game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    #detect collision with wall  
    if ball.ycor() > 279 or ball.ycor() < -279:
        ball.bounce_y()

    #detect collision with paddles  
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320 or ball.distance(left_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.increase_left_score()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.increase_right_score()
    
    





screen.exitonclick()