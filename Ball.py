from turtle import Turtle

class Ball(Turtle):
    
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=1)
        
    def move(self):
        self.goto(self.xcor()+10, self.ycor()+10)