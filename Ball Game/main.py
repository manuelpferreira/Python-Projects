from turtle import Screen
from padle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

paddle_r = Paddle((350, 0))
paddle_l = Paddle((-350, 0))
ball = Ball()
score = ScoreBoard()

screen.listen()
screen.onkeypress(paddle_r.go_up, "Up")
screen.onkeypress(paddle_r.go_down, "Down")
screen.onkeypress(paddle_l.go_up, "w")
screen.onkeypress(paddle_l.go_down, "s")


game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.around()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(paddle_r) < 50 and ball.xcor() > 320 or ball.distance(paddle_l) < 50 or ball.xcor() < -320:
        ball.bounce_x()

    if ball.xcor() > 380:
        ball.reset_position()
        score.left_point()

    if ball.ycor() < -380:
        ball.reset_position()
        score.right_point()


screen.exitonclick()
