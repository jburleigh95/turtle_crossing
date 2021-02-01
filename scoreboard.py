from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('black')
        self.hideturtle()
        self.penup()
        self.level = 1
        self.goto(-280, 250)
        self.write_score()

    def write_score(self):
        self.clear()
        self.write(f"Level: {self.level}", align='left', font=('Courier', 20, 'normal'))

    def update_score(self):
        self.level += 1
        self.write_score()

    def end_game(self):
        self.home()
        self.write("GAME OVER", align='center', font=('Courier', 20, 'normal'))