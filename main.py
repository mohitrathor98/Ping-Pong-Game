from turtle import Screen, left
from paddle import Paddle
from ball import Ball

import time

from scoreboard import Scoreboard

# screen setup
screen = Screen()
screen.setup(height = 600, width = 800)
screen.bgcolor("black")
screen.title("Ping-Pong")
screen.tracer(0)

# paddle creation and move
right_paddle = Paddle((360, 0))
left_paddle = Paddle((-360, 0))

ball = Ball()
scoreboard = Scoreboard()

screen.listen()

screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()
    
    # detect collision with top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()
        
    # detect collision with paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        ball.move_speed *= 0.9 # increases ball speed
        
    # detect paddle miss
    if ball.xcor() > 380: 
        ball.goto(0,0)
        ball.bounce_x()
        scoreboard.l_update()
        ball.move_speed = 0.1
        
    if ball.xcor() < -380:
        ball.goto(0,0)
        ball.bounce_x() 
        scoreboard.r_update()

screen.exitonclick()