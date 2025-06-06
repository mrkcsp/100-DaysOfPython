from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 80, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.left_score = 0
        self.right_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align=ALIGNMENT, font=FONT)
        self.goto(100, 200)
        self.write(self.right_score, align=ALIGNMENT, font=FONT)

    def increase_left_score(self):
        self.left_score +=1
        self.update_scoreboard()
    
    def increase_right_score(self):
        self.right_score +=1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)
