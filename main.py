from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width = 800, height = 600 )
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")


game_is_on = True
speed = 0.07
while game_is_on:

    time.sleep(speed)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(r_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()
        speed *= 0.95

    if ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()
        speed *= 0.95

    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()
        speed = 0.07

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        speed = 0.07

    if speed == 0.01:
        speed += 0.01
screen.exitonclick()