from turtle import Turtle

class Sprite(Turtle):
    def __init__(self, shape, color, x, y, sign):
        super().__init__(shape)
        self.color(color)
        self.speed(0)
        self.penup()
        self.goto(x, y)
        self.sign = sign
        self.dx = 0
        self.dy = 0
        self.prevdx = 0
        self.prevdy = 0

