from turtle import Turtle

class Button(Turtle):
    def __init__(self, shape, wid, len, color, x, y, onclick):
        super().__init__(shape)
        self.shapesize(wid, len)
        self.color(color)
        self.onclick(onclick)
        self.penup()
        self.goto(x, y)

    def setSize(self, wid, len):
        self.shapesize(wid, len)

    def moveButton(self, x, y):
        self.goto(x, y)
        
    def setColor(self, color):
        self.color(color)

class ControlButton(Button):
    def __init__(self, label, shape, wid, len, color, x, y, label_y, onclick):
        super().__init__(shape, wid, len, color, x, y, onclick)
        self.toggle = False 
        self.goto(x, label_y)
        self.write(f'{label}', align='center', font=("Courier", 18, "normal"))
        self.goto(x, y)
    
    def isActive(self):
        return self.toggle 
    
    def clearPen(self, x, y):
        self.clear()
        self.penup()
        self.goto(x, y) 

    def updateLabel(self, label):
        self.write(f'{label}', align='center', font=("Courier", 18, "normal")) 

    def resetToPause(self, x, y, label_y):
        self.clearPen(x, label_y)
        self.updateLabel('Pause')
        self.write('Pause', align='center', font=("Courier", 18, "normal"))
        self.goto(x, y)
        self.toggle = False

    def toggleStatus(self):
        self.toggle = not self.toggle


class ReverseButton(Button):
    def __init__(self, shape, wid, len, color, x, y, onclick, angle, width):
        super().__init__(shape, wid, len, color, x, y, onclick)
        self.width(width)
        self.pendown()
        self.right(angle)
        self.forward(20) 

class RestartButton(Button):
    def __init__(self, label, shape, wid, len, color, x, y, label_y, onclick):
        super().__init__(shape, wid, len, color, x, y, onclick)
        self.hideturtle()
        self.label = label
        self.x = x
        self.y = y
        self.label_y = label_y 

    def restart(self):
        self.goto(self.x, self.label_y)
        self.write(f'{self.label}', align='center', font=("Courier", 18, "normal"))
        self.goto(self.x, self.y)
        self.showturtle()
    
    def removeButton(self):
        self.clear()
        self.hideturtle()

