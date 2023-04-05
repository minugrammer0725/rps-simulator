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
    
    def moveSprite(self):
        self.setx(self.xcor() + self.dx)
        self.sety(self.ycor() + self.dy)

    def checkBorders(self, top, btm, right, left):
        # right, left
        if self.xcor() > right:
            self.setx(right)
            self.dx *= -1
        elif self.xcor() < left:
            self.setx(left)
            self.dx *= -1
        # top, bottom
        if self.ycor() > top:
            self.sety(top)
            self.dy *= -1
        elif self.ycor() < btm:
            self.sety(btm)
            self.dy *= -1
    
    def hideSprite(self):
        self.hideturtle()
    def showSprite(self):
        self.showturtle()

    def getSign(self):
        return self.sign 
    def setSign(self, sign):
        self.sign = sign 
    
    def getDx(self):
        return self.dx
    def setDx(self, dx):
        self.dx = dx

    def getDy(self):
        return self.dy
    def setDy(self, dy):
        self.dy = dy

    def getPrevDx(self):
        return self.prevdx
    def setPrevDx(self, prevdx):
        self.prevdx = prevdx

    def getPrevDy(self):
        return self.prevdy
    def setPrevDy(self, prevdy):
        self.prevdy = prevdy

    def setColor(self, color):
        self.color(color) 

    