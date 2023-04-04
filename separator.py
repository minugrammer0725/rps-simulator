from turtle import Turtle

class Separator(Turtle):

  def __init__(self, x, y, color, width, screen_height):
      super().__init__()
      self.color(color)
      self.width(width)
      self.hideturtle()
      self.penup()
      self.goto(x, y)
      self.pendown()
      self.right(90)
      self.forward(screen_height)

