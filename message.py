from turtle import Turtle

class Message(Turtle):
    def __init__(self, speed, x, y):
        super().__init__()
        self.speed(speed)
        self.penup()
        self.hideturtle()
        self.goto(x, y)       

    def clearMessage(self):
        self.clear()

    def writeMessage(self, msg, wn, timeout):
        self.clear()
        self.write(f'{msg}', align='center', font=('Courier', 18, 'normal'))
        wn.ontimer(lambda: self.clear(), timeout)

    def gameOver(self):
        self.clear
        self.write('Game Over!', align='center', font=('Courier', 18, 'normal'))

        