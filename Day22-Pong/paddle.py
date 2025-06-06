from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.create_paddle(position)

    def create_paddle(self, position):
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.goto(position)
            
    def go_up(self):
        if self.ycor() < 300:
            new_y= self.ycor() + 20
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > -300:
            new_y= self.ycor() - 20
            self.goto(self.xcor(), new_y)


    



