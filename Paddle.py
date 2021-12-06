from turtle import Turtle

class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid= 5, stretch_len= 1)
        self.goto(position)
    
    def up(self):
        if self.ycor() < 240:
            self.sety(self.position()[1]+20)
    
    def down(self):
        if self.ycor() > -240:
            self.sety(self.position()[1]-20)