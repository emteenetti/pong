from turtle import Turtle

FONT = ("Courier", 24, "normal")
ALIGNMENT = "center"


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.goto(0, 420)
        self.hideturtle()
        self.player1_score = 0
        self.player2_score = 0
        self.write(f"PLAYER 1: {self.player1_score} PLAYER 2: {self.player2_score}", move=False, align=ALIGNMENT,
                   font=FONT)

    def player1(self):
        self.player1_score += 1
        self.clear()
        self.write(f"PLAYER 1: {self.player1_score} PLAYER 2: {self.player2_score}", move=False, align=ALIGNMENT,
                   font=FONT)

    def player2(self):
        self.player2_score += 1
        self.clear()
        self.write(f"PLAYER 1: {self.player1_score} PLAYER 2: {self.player2_score}", move=False, align=ALIGNMENT,
                   font=FONT)

    def gameOver(self):
        if self.player1_score > self.player2_score:
            self.clear()
            self.write(f"PLAYER 1: {self.player1_score} PLAYER 2: {self.player2_score} PLAYER 1 WINS!", move=False,
                       align=ALIGNMENT,
                       font=FONT)
        else:
            self.clear()
            self.write(f"PLAYER 1: {self.player1_score} PLAYER 2: {self.player2_score} PLAYER 2 WINS!", move=False,
                       align=ALIGNMENT,
                       font=FONT)
