from turtle import Screen, left
from Paddle import Paddle
from Ball import Ball

import time

# screen setup
screen = Screen()
screen.setup(height = 600, width = 800)
screen.bgcolor("black")
screen.title("Ping-Pong")
screen.tracer(0)

'''
TODO:

1) Create and move a paddle == done
2) Create another paddle == done
3) create the ball and make it move == done
4) Detect collision with top & bottom walls and bounce == done
5) Detect collision with paddle == done
6) Detect when paddle misses == done
7) Keep score
'''

# paddle creation and move
right_paddle = Paddle((360, 0))
left_paddle = Paddle((-360, 0))

ball = Ball()

screen.listen()

screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")

screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    ball.move()
    
    # detect collision with top or bottom wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()
        
    # detect collision with paddle
    if (ball.distance(right_paddle) < 50 and ball.xcor() > 320) or (ball.distance(left_paddle) < 50 and ball.xcor() < -320):
        ball.bounce_x()
        
    # detect paddle miss
    if ball.xcor() > 380 or ball.xcor() < -380:
        ball.goto(0,0)
        ball.bounce_x() 

screen.exitonclick()