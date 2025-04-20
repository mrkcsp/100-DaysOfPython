from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.create_player()

    def create_player(self):
        self.shape("turtle")
        self.left(90)
        self.penup()
        self.go_to_start()

    def go_up(self):
        if self.ycor() < FINISH_LINE_Y:
            new_y= self.ycor() + MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def go_down(self):
        if self.ycor() > -FINISH_LINE_Y:
            new_y= self.ycor() - MOVE_DISTANCE
            self.goto(self.xcor(), new_y)

    def is_at_finish(self):
        if self.ycor() >= FINISH_LINE_Y:
            return True
        else:
            return False
    
    def go_to_start(self):
        self.goto(STARTING_POSITION)
