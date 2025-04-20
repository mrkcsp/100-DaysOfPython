from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Arial', 24, 'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(0, 260)
        self.read_highScore()
        self.update_scoreboard()
    
    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} - High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score +=1
        self.update_scoreboard()

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.write_highScore()
        self.score = 0
        self.update_scoreboard()

    def read_highScore(self):
        with open("data.txt") as file:
            data = file.read()
            if data == "":
                self.high_score = 0
            else:
                self.high_score = int(data)

    def write_highScore(self):
        with open("data.txt", mode="w") as file:
            data = str(self.high_score)
            file.write(data)
       
