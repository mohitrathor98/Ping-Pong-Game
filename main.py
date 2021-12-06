from turtle import Screen
import turtle
from Paddle import Paddle

# screen setup
screen = Screen()
screen.setup(height = 600, width = 800)
screen.bgcolor("black")
screen.title("Ping-Pong")
screen.tracer(0)

'''
TODO:

1) Create and move a paddle == done
2) Create another paddle
3) create the ball and make it move
4) Detect collision with wall and bounce
5) Detect collision with paddle
6) Detect when paddle misses
7) Keep score
'''

# paddle creation and move
right_paddle = Paddle((360, 0))


turtle.listen()
turtle.onkey(right_paddle.up, "Up")
turtle.onkey(right_paddle.down, "Down")


game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()