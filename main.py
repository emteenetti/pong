from turtle import Screen, Turtle
from player import Paddle
from ball import Ball
from scoreboard import Scoreboard

# import time

screen = Screen()
screen.tracer(0)
border = Turtle()
border.hideturtle()
border.penup()
border.pensize(3)
border.pencolor("blue")
border.goto(-400, 400)
border.pendown()
for i in range(4):
    border.forward(800)
    border.right(90)
border.penup()
partition = Turtle()
ball = Ball()
scoreboard = Scoreboard()
screen.bgcolor("white")
partition.hideturtle()
partition.penup()
partition.pencolor("blue")
screen.setup(width=800, height=800)
screen_height = screen.window_height()
screen_width = screen.window_width()
partition.goto(0, screen_width // 2)
partition.setheading(270)
partition.pensize(5)
gameOn = True

for _ in range(screen_height):
    partition.forward(10)
    if _ % 2 == 0:
        partition.pendown()
    else:
        partition.penup()

player_1 = []
player_2 = []
for i in range(3):
    y1 = (i - 2) * 30  # Adjust y-coordinate for each paddle
    position = (370, y1)
    paddle1 = Paddle()
    paddle1.goto(position)
    player_1.append(paddle1)

for i in range(3):
    y2 = (i - 2) * 30
    position = (-370, y2)
    paddle2 = Paddle()
    paddle2.goto(position)
    player_2.append(paddle2)

screen.update()
screen.listen()


def mover1():
    if player_1[2].ycor() < 390:
        player_1[0].move_up()
        player_1[1].move_up()
        player_1[2].move_up()
    else:
        pass
    screen.update()


def downer1():
    if player_1[2].ycor() > -390:
        player_1[0].move_down()
        player_1[1].move_down()
        player_1[2].move_down()
    else:
        pass
    screen.update()


def mover2():
    if player_2[2].ycor() < 390:
        player_2[0].move_up()
        player_2[1].move_up()
        player_2[2].move_up()
    else:
        pass
    screen.update()


def downer2():
    if player_2[2].ycor() > -390:
        player_2[0].move_down()
        player_2[1].move_down()
        player_2[2].move_down()
    else:
        pass
    screen.update()


screen.onkey(mover2, "w")
screen.onkey(downer2, "s")

screen.onkey(mover1, "Up")
screen.onkey(downer1, "Down")

while gameOn:
    ball.movominento()
    screen.update()

    # top and bottom collision detection
    if ball.ycor() > 390 or ball.ycor() < - 390:
        ball.bounce_y()

    for paddle in player_1:
        if ball.distance(paddle) < 15:
            ball.bounce_x()

    for paddle in player_2:
        if ball.distance(paddle) < 15:
            ball.bounce_x()

    if ball.xcor() > 400:
        ball.reset()
        ball.bounce_x()
        scoreboard.player2()
    if ball.xcor() < - 400:
        ball.reset()
        ball.bounce_x()
        scoreboard.player1()
    if scoreboard.player2_score == 10 or scoreboard.player1_score == 10:
        gameOn = False
        scoreboard.gameOver()

screen.exitonclick()
