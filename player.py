from turtle import Turtle, Screen

screen = Screen()
screen.tracer(0)


class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1.5, stretch_len=1)
        self.penup()
        self.color("blue")
        # self.moveup()
        # self.movedown()
        # if player == 2:
        #     self.X_axes = 370
        # else:
        #     self.X_axes = -370
        # self.Y_axes = 0
        # self.goto(self.X_axes, self.Y_axes)
        # screen.update()

    def move_up(self):
        self.sety(self.ycor() + 30)

    def move_down(self):
        self.sety(self.ycor() - 30)


# p1 = Paddle()
# screen.listen()
# screen.onkey(p1.moveup, "Up")
# screen.onkey(p1.movedown, "Down")
# screen.exitonclick()
