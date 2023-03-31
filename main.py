'''
TODO:
1) Add Start button
2) Combine Pause/Resume into one button -> update the message
'''

from turtle import Turtle, Screen
from random import randint

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
BOARD_WIDTH = 700
CONTROLS_WIDTH = 300
BALL_WIDTH = 20

top_border = SCREEN_HEIGHT/2 - BALL_WIDTH/2
bottom_border = BALL_WIDTH/2 - SCREEN_HEIGHT/2
right_border = SCREEN_WIDTH/2 - CONTROLS_WIDTH - BALL_WIDTH/2
left_border = BALL_WIDTH/2 - SCREEN_WIDTH/2

def onWindowClick(x, y):
    # if (x, y) is within board borders, summon a ball
    if left_border <= x <= right_border and bottom_border <= y <= top_border:
        ball = Turtle(shape='circle')
        ball.color('blue')
        ball.speed(0)
        ball.dx = 0
        ball.dy = 0
        ball.prevdx = 0
        ball.prevdy = 0
        ball.penup()
        ball.goto(x, y)
        balls.append(ball)


wn = Screen()
wn.title('RPS-Simulator')
wn.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
wn.bgcolor('#D3D3D3')
wn.tracer(0)
wn.listen()
wn.onclick(onWindowClick)
wn._root.resizable(False, False)
 
# draw a line for controls panel
separator = Turtle()
separator.color('black')
separator.width(4)
separator.hideturtle()
separator.penup()
separator.goto(200, 300)
separator.pendown()
separator.right(90)
separator.forward(600)

# click events
def onStartClick(x, y):
    for ball in balls:
        ball.dx = options[randint(0,1)]
        ball.dy = options[randint(0,1)]

def onPauseResumeToggle(x, y):
    pass 


def onPauseClick(x, y):
    for ball in balls:
        ball.prevdx = ball.dx
        ball.prevdy = ball.dy
        ball.dx = 0
        ball.dy = 0
def onResumeClick(x,y):
    for ball in balls:
        ball.dx = ball.prevdx
        ball.dy = ball.prevdy


start_button = Turtle()
start_button.shape('square')
start_button.shapesize(2, 3)
start_button.color('purple')
start_button.penup()
start_button.goto(350, 240)
start_button.write('Start', align='center', font=("Courier", 18, "normal"))
start_button.goto(350, 220)
start_button.onclick(onStartClick)


pause_button = Turtle()
pause_button.shape('square')
pause_button.shapesize(2, 3)
pause_button.color('green')
pause_button.penup()
pause_button.goto(350, 170)
pause_button.write('Pause', align='center', font=("Courier", 18, "normal"))
pause_button.goto(350, 150)
pause_button.onclick(onPauseClick)

resume_button = Turtle()
resume_button.shape('square')
resume_button.shapesize(2,3)
resume_button.color('blue')
resume_button.penup()
resume_button.goto(350, 100)
resume_button.write('Resume', align='center', font=("Courier", 18, "normal"))
resume_button.goto(350, 80)
resume_button.onclick(onResumeClick)

# all balls on the screen
balls = []

# intial dx, dy values
options = [0.2, -0.2]

# game loop
while True:
    wn.update()

    for ball in balls:
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)
        # check borders
        if ball.xcor() > right_border:
            ball.setx(right_border)
            ball.dx *= -1
        elif ball.xcor() < left_border:
            ball.setx(left_border)
            ball.dx *= -1
        if ball.ycor() > top_border:
            ball.sety(top_border)
            ball.dy *= -1
        elif ball.ycor() < bottom_border:
            ball.sety(bottom_border)
            ball.dy *= -1
