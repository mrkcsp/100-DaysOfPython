from turtle import Turtle

STARTING_POSITIONS = [(0,0),(-20, 0), (-40,0)]
MOVE_DISTANCE = 20

UP=90
DOWN=270
LEFT=180
RIGHT=0

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            
    def add_segment(self, position):
        newPiece = Turtle(shape="square")
        newPiece.color("white")
        newPiece.penup()
        newPiece.goto(position)
        self.segments.append(newPiece)

    def extend(self):
        self.add_segment(self.segments[-1].position())
    
    def move_snake(self):
        for piece in range(len(self.segments) - 1, 0 , -1):
            new_x = self.segments[piece - 1].xcor()
            new_y = self.segments[piece - 1].ycor()
            self.segments[piece].goto(new_x, new_y)
        self.segments[0].forward(MOVE_DISTANCE)

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



