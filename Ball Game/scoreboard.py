from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.score_left = 0
        self.score_right = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.goto(-100, 200)
        self.write(self.score_left, align="center", font=("Courier", 80, "normal"))
        self.goto(100, 200)
        self.write(self.score_right, align="center", font=("Courier", 80, "normal"))

    def left_point(self):
        self.clear()
        self.score_left += 1
        self.update_scoreboard()

    def right_point(self):
        self.score_right += 1
        self.update_scoreboard()

