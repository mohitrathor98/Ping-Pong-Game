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
4) Detect collision with top & bottom walls and bounce
5) Detect collision with paddle
6) Detect when paddle misses
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

screen.exitonclick()