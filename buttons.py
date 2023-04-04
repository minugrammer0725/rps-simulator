from turtle import Turtle

class Button(Turtle):
    def __init__(self, shape, wid, len, color, x, y, onclick):
        super().__init__(shape)
        self.shapesize(wid, len)
        self.color(color)
        self.onclick(onclick)
        self.penup()
        self.goto(x, y)


class ControlButton(Button):
    def __init__(self, label, shape, wid, len, color, x, y, label_y, onclick):
        super().__init__(shape, wid, len, color, x, y, onclick)
        self.toggle = False 
        self.goto(x, label_y)
        self.write(f'{label}', align='center', font=("Courier", 18, "normal"))
        self.goto(x, y)

        
class ReverseButton(Button):
    def __init__(self, shape, wid, len, color, x, y, onclick, angle, width):
        super().__init__(shape, wid, len, color, x, y, onclick)
        self.width(width)
        self.pendown()
        self.right(angle)
        self.forward(20) 

