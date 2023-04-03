from turtle import Turtle, Screen
from random import randint
from time import sleep

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
BOARD_WIDTH = 700
CONTROLS_WIDTH = 300
BALL_WIDTH = 20
INIT_SPEED = 0.5

top_border = SCREEN_HEIGHT/2 - BALL_WIDTH/2
bottom_border = BALL_WIDTH/2 - SCREEN_HEIGHT/2
right_border = SCREEN_WIDTH/2 - CONTROLS_WIDTH - BALL_WIDTH/2
left_border = BALL_WIDTH/2 - SCREEN_WIDTH/2

# all balls on the screen
balls = []
# copy array used for undo/redo
copy = []

# intial dx, dy values
options = [INIT_SPEED, -INIT_SPEED]

def onWindowClick(x, y):
    # if (x, y) is within board borders, summon a ball
    if not(left_border <= x <= right_border and bottom_border <= y <= top_border and not start_stop_button.started):
        return

    # python match: 3.10 >
    match wn.selected:
        case 'rock':
            rock = Turtle(shape='circle')
            rock.color('red')
            rock.speed(0)
            rock.dx = 0
            rock.dy = 0
            rock.prevdx = 0
            rock.prevdy = 0
            rock.penup()
            rock.goto(x, y)
            balls.append(rock)
        case 'paper':
            paper = Turtle(shape='square')
            paper.color('green')
            paper.speed(0)
            paper.dx = 0
            paper.dy = 0
            paper.prevdx = 0
            paper.prevdy = 0
            paper.penup()
            paper.goto(x, y)
            balls.append(paper)
        case 'scissor':
            scissor = Turtle(shape='triangle')
            scissor.color('blue')
            scissor.speed(0)
            scissor.dx = 0
            scissor.dy = 0
            scissor.prevdx = 0
            scissor.prevdy = 0
            scissor.penup()
            scissor.goto(x, y)
            balls.append(scissor)
        case _:
            message.clear()
            message.write('Please select a color.', align="center", font=("Courier", 14, "normal"))
            wn.ontimer(lambda: message.clear(), 2000)

    


wn = Screen()
wn.title('RPS-Simulator')
wn.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
wn.bgcolor('#D3D3D3')
wn.tracer(0)
wn.listen()
wn.onclick(onWindowClick)
wn.selected = None
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


message = Turtle()
message.speed(0)
message.penup()
message.hideturtle()
message.goto(-150, 200)


# click events
def onStartStopToggle(x, y):
    if len(balls) < 1:
        message.clear()
        message.write('Summon at least one sprite into the screen.', align="center", font=("Courier", 14, "normal"))
        wn.ontimer(lambda: message.clear(), 2500)
        return
    start_stop_button.clear()
    start_stop_button.penup()
    start_stop_button.goto(350, 180)
    if start_stop_button.started:
        start_stop_button.write('Start', align='center', font=("Courier", 18, "normal"))
        for ball in balls:
            ball.hideturtle()
        balls.clear()
        # after game has stopped, the pause/resume button should be on pause.
        pause_resume_button.clear()
        pause_resume_button.penup()
        pause_resume_button.goto(350, 110)
        pause_resume_button.write('Pause', align='center', font=("Courier", 18, "normal"))
        pause_resume_button.goto(350, 90)
        pause_resume_button.paused = False

    else:
        start_stop_button.write('Stop', align='center', font=("Courier", 18, "normal"))
        for ball in balls:
            ball.dx = options[randint(0,1)]
            ball.dy = options[randint(0,1)]
    start_stop_button.goto(350, 160)
    start_stop_button.started = not start_stop_button.started
    # reset summon buttons
    wn.selected = None
    rock_button.shapesize(2.1, 2.1)
    paper_button.shapesize(2.1, 2.1)
    scissor_button.shapesize(2.1, 2.1)
    # empty copy array
    copy.clear()

def onPauseResumeToggle(x, y):
    if not start_stop_button.started:
        message.clear()
        message.write('Game has not started yet.', align="center", font=("Courier", 14, "normal"))
        wn.ontimer(lambda: message.clear(), 2500)
        return
    pause_resume_button.clear()
    pause_resume_button.penup()
    pause_resume_button.goto(350, 110)
    if pause_resume_button.paused:
        pause_resume_button.write('Pause', align='center', font=("Courier", 18, "normal"))
        for ball in balls:
            ball.dx = ball.prevdx
            ball.dy = ball.prevdy
    else:
        pause_resume_button.write('Resume', align='center', font=("Courier", 18, "normal"))
        for ball in balls:
            ball.prevdx = ball.dx
            ball.prevdy = ball.dy
            ball.dx = 0
            ball.dy = 0
    pause_resume_button.goto(350, 90)
    pause_resume_button.paused = not pause_resume_button.paused

def summon_rock(x, y):
    if start_stop_button.started:
        return
    wn.selected = 'rock'
    rock_button.shapesize(2.5, 2.5)
    paper_button.shapesize(2.1,2.1)
    scissor_button.shapesize(2.1, 2.1)

def summon_paper(x, y):
    if start_stop_button.started:
        return
    wn.selected = 'paper'
    rock_button.shapesize(2.1, 2.1)
    paper_button.shapesize(2.5,2.5)
    scissor_button.shapesize(2.1, 2.1)

def summon_scissor(x, y):
    if start_stop_button.started:
        return
    wn.selected = 'scissor'
    rock_button.shapesize(2.1, 2.1)
    paper_button.shapesize(2.1,2.1)
    scissor_button.shapesize(2.5, 2.5)


def onUndoClick(x, y):
    # check if data arr is non-empty
    if start_stop_button.started:
        return 
    if len(balls) < 1:
        message.clear()
        message.write('Cannot Undo.', align="center", font=("Courier", 14, "normal"))
        wn.ontimer(lambda: message.clear(), 2000)
        return
    ball = balls.pop()
    ball.hideturtle()
    copy.append(ball)
     

def onRedoClick(x, y):
    # check if copy arr is non-empty
    if start_stop_button.started:
        return 
    if len(copy) < 1:
        message.clear()
        message.write('Cannot Redo.', align="center", font=("Courier", 14, "normal"))
        wn.ontimer(lambda: message.clear(), 2000)
        return
    ball = copy.pop()
    ball.showturtle() 
    balls.append(ball)
     


start_stop_button = Turtle()
start_stop_button.shape('square')
start_stop_button.shapesize(2, 3)
start_stop_button.color('purple')
start_stop_button.penup()
start_stop_button.goto(350, 180)
start_stop_button.write('Start', align='center', font=("Courier", 18, "normal"))
start_stop_button.goto(350, 160)
start_stop_button.started = False
start_stop_button.onclick(onStartStopToggle)


pause_resume_button = Turtle()
pause_resume_button.shape('square')
pause_resume_button.shapesize(2, 3)
pause_resume_button.color('#624a2e')
pause_resume_button.penup()
pause_resume_button.goto(350, 110)
pause_resume_button.write('Pause', align='center', font=("Courier", 18, "normal"))
pause_resume_button.goto(350, 90)
pause_resume_button.paused = False
pause_resume_button.onclick(onPauseResumeToggle)


# rock, paper, scissor sprites
rock_button = Turtle()
rock_button.shape('circle')
rock_button.shapesize(2.1, 2.1)
rock_button.color('red')
rock_button.penup()
rock_button.goto(270, 240)
rock_button.onclick(summon_rock)

paper_button = Turtle()
paper_button.shape('circle')
paper_button.shapesize(2.1, 2.1)
paper_button.color('green')
paper_button.penup()
paper_button.goto(350, 240)
paper_button.onclick(summon_paper)

scissor_button = Turtle()
scissor_button.shape('circle')
scissor_button.shapesize(2.1, 2.1)
scissor_button.color('blue')
scissor_button.penup()
scissor_button.goto(430, 240)
scissor_button.onclick(summon_scissor)


# TODO: Collision Detection using turtle.distance() and math methods..
# def isCollision(t1, t2): return t1.distance(t2) < COLLISION_CONSTANT(i.e. 20)

# TODO: Undo/Redo buttons
undo_button = Turtle()
undo_button.shape('arrow')
undo_button.shapesize(1, 2)
undo_button.width(5)
undo_button.right(180)
undo_button.shapesize()
undo_button.color('grey')
undo_button.penup()
undo_button.goto(330, -50)
undo_button.pendown()
undo_button.forward(20)
undo_button.onclick(onUndoClick)


redo_button = Turtle()
redo_button.shape('arrow')
redo_button.shapesize(1, 2)
redo_button.width(5)
redo_button.shapesize()
redo_button.color('grey')
redo_button.penup()
redo_button.goto(370, -50)
redo_button.pendown()
redo_button.forward(20)
redo_button.onclick(onRedoClick)




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
    
    if len(balls) < 1 or start_stop_button.started:
        undo_button.color('grey')
    else:
        undo_button.color('black')

    if len(copy) < 1 or start_stop_button.started:
        redo_button.color('grey')
    else:
        redo_button.color('black')
