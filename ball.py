from turtle import Turtle



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.color("blue")
        self.penup()
        self.goto(0, 0)
        self.stepX = 3
        self.stepY = 4

    def movominento(self):
        new_x = self.xcor() + self.stepX
        new_y = self.ycor() + self.stepY
        self.goto(new_x, new_y)

    def reset(self):
        self.goto(0, 0)

    def bounce_x(self):
        self.stepX *= -1

    def bounce_y(self):
        self.stepY *= -1
    def bounce_down(self):
       if self.stepY > 0:
           self.stepY *= -1
       else:
           pass
    def bounce_up(self):
       if self.stepY < 0:
           self.stepY *= -1
       else:
           pass