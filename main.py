from turtle import Turtle, Screen
from random import randint

from separator import Separator
from message import Message
from sprite import Sprite
from buttons import Button, ControlButton, ReverseButton

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 600
BOARD_WIDTH = 700
CONTROLS_WIDTH = 300
SPRITE_WIDTH = 20
INIT_SPEED = 1

COLLISION_RADIUS = 15

TOP_BORDER = SCREEN_HEIGHT/2 - SPRITE_WIDTH/2
BOTTOM_BORDER = SPRITE_WIDTH/2 - SCREEN_HEIGHT/2
RIGHT_BORDER = SCREEN_WIDTH/2 - CONTROLS_WIDTH - SPRITE_WIDTH/2
LEFT_BORDER = SPRITE_WIDTH/2 - SCREEN_WIDTH/2

MESSAGE_TIMEOUT = 1700

SEPARATOR_X = 200
SEPARATOR_Y = 300

MESSAGE_X = -150
MESSAGE_Y = 200

SS_BUTTON_X = 350
SS_BUTTON_Y = 160
SS_BUTTON_TEXT_Y = 180

PR_BUTTON_X = 350 
PR_BUTTON_Y = 90
PR_BUTTON_TEXT_Y = 110

SUMMON_BTN_SIZE = 2.1
SUMMON_BTN_HOVER = 2.5
SUMMON_BTN_Y = 240

ROCK_BTN_X = 270
PAPER_BTN_X = 350
SCISSOR_BTN_X = 430

UNDO_BTN_X = 330
UNDO_BTN_Y = -50

REDO_BTN_X = 370
REDO_BTN_Y = -50


# all sprites on the screen
sprites = []
# copy array used for undo/redo
copy = []

# intial dx, dy values
options = [INIT_SPEED, -INIT_SPEED]

def onWindowClick(x, y):
    # if (x, y) is within board borders, summon a sprite
    if not(LEFT_BORDER <= x <= RIGHT_BORDER and BOTTOM_BORDER <= y <= TOP_BORDER and not start_stop_button.toggle):
        return

    # python match: 3.10 >
    match wn.selected:
        case 'rock':
            rock = Sprite('circle', 'red', x, y, 'rock')
            sprites.append(rock)
        case 'paper':
            paper = Sprite('square', 'green', x, y, 'paper')
            sprites.append(paper)
        case 'scissor':
            scissor = Sprite('triangle', 'blue', x, y, 'scissor')
            sprites.append(scissor)
        case _:
            message.writeMessage('Please Select a Color', wn, MESSAGE_TIMEOUT)

def canStart():
    if len(sprites) < 2 or notEnoughUniqueItems():
        return False
    return True

def notEnoughUniqueItems():
    sign = sprites[0].sign
    count = 0
    for sprite in sprites:
        if sign == sprite.sign:
            count += 1
    return True if count == len(sprites)  else False


wn = Screen()
wn.title('RPS-Simulator')
wn.setup(width=SCREEN_WIDTH, height=SCREEN_HEIGHT)
wn.bgcolor('#D3D3D3')
wn.tracer(0)
wn.listen()
wn.onclick(onWindowClick)
wn.selected = None
wn._root.resizable(False, False)
 
# separator component to divide game board and controls
separator = Separator(SEPARATOR_X, SEPARATOR_Y, 'yellow', 4, SCREEN_HEIGHT)
# message component to alert user
message = Message(0, MESSAGE_X, MESSAGE_Y)


# click events
def onStartStopToggle(x, y):
    if not canStart():
        message.writeMessage('Summon at least 2 different items', wn, MESSAGE_TIMEOUT)
        return
    start_stop_button.clear()
    start_stop_button.penup()
    start_stop_button.goto(SS_BUTTON_X, SS_BUTTON_TEXT_Y)
    if start_stop_button.toggle:
        start_stop_button.write('Start', align='center', font=("Courier", 18, "normal"))
        for sprite in sprites:
            sprite.hideturtle()
        sprites.clear()
        # after game has stopped, the pause/resume button should be on pause.
        pause_resume_button.clear()
        pause_resume_button.penup()
        pause_resume_button.goto(PR_BUTTON_X, PR_BUTTON_TEXT_Y)
        pause_resume_button.write('Pause', align='center', font=("Courier", 18, "normal"))
        pause_resume_button.goto(PR_BUTTON_X, PR_BUTTON_Y)
        pause_resume_button.toggle = False

    else:
        message.clearMessage()
        start_stop_button.write('Stop', align='center', font=("Courier", 18, "normal"))
        for sprite in sprites:
            sprite.dx = options[randint(0,1)]
            sprite.dy = options[randint(0,1)]
    start_stop_button.goto(SS_BUTTON_X, SS_BUTTON_Y)
    start_stop_button.toggle = not start_stop_button.toggle
    # reset summon buttons
    wn.selected = None
    rock_button.shapesize(SUMMON_BTN_SIZE, SUMMON_BTN_SIZE)
    paper_button.shapesize(SUMMON_BTN_SIZE, SUMMON_BTN_SIZE)
    scissor_button.shapesize(SUMMON_BTN_SIZE, SUMMON_BTN_SIZE)
    # empty copy array
    copy.clear()

def onPauseResumeToggle(x, y):
    if not start_stop_button.toggle:
        message.writeMessage('Game has not started yet', wn, MESSAGE_TIMEOUT)
        return
    pause_resume_button.clear()
    pause_resume_button.penup()
    pause_resume_button.goto(PR_BUTTON_X, PR_BUTTON_TEXT_Y)
    if pause_resume_button.toggle:
        pause_resume_button.write('Pause', align='center', font=("Courier", 18, "normal"))
        for sprite in sprites:
            sprite.dx = sprite.prevdx
            sprite.dy = sprite.prevdy
    else:
        pause_resume_button.write('Resume', align='center', font=("Courier", 18, "normal"))
        for sprite in sprites:
            sprite.prevdx = sprite.dx
            sprite.prevdy = sprite.dy
            sprite.dx = 0
            sprite.dy = 0
    pause_resume_button.goto(PR_BUTTON_X, PR_BUTTON_Y)
    pause_resume_button.toggle = not pause_resume_button.toggle

def summon_rock(x, y):
    if start_stop_button.toggle:
        return
    wn.selected = 'rock'
    rock_button.shapesize(SUMMON_BTN_HOVER, SUMMON_BTN_HOVER)
    paper_button.shapesize(SUMMON_BTN_SIZE,SUMMON_BTN_SIZE)
    scissor_button.shapesize(SUMMON_BTN_SIZE, SUMMON_BTN_SIZE)

def summon_paper(x, y):
    if start_stop_button.toggle:
        return
    wn.selected = 'paper'
    rock_button.shapesize(SUMMON_BTN_SIZE, SUMMON_BTN_SIZE)
    paper_button.shapesize(SUMMON_BTN_HOVER,SUMMON_BTN_HOVER)
    scissor_button.shapesize(SUMMON_BTN_SIZE, SUMMON_BTN_SIZE)

def summon_scissor(x, y):
    if start_stop_button.toggle:
        return
    wn.selected = 'scissor'
    rock_button.shapesize(SUMMON_BTN_SIZE, SUMMON_BTN_SIZE)
    paper_button.shapesize(SUMMON_BTN_SIZE,SUMMON_BTN_SIZE)
    scissor_button.shapesize(SUMMON_BTN_HOVER, SUMMON_BTN_HOVER)


def onUndoClick(x, y):
    # check if data arr is non-empty
    if start_stop_button.toggle:
        return 
    if len(sprites) < 1:
        message.writeMessage('Cannot Undo', wn, MESSAGE_TIMEOUT)
        return
    sprite = sprites.pop()
    sprite.hideturtle()
    copy.append(sprite)
     

def onRedoClick(x, y):
    # check if copy arr is non-empty
    if start_stop_button.toggle:
        return 
    if len(copy) < 1:
        message.writeMessage('Cannot Redo', wn, MESSAGE_TIMEOUT)
        return
    sprite = copy.pop()
    sprite.showturtle() 
    sprites.append(sprite)


def detectCollision():
    indices = []
    for i in range(len(sprites)):
        for j in range(i+1, len(sprites)):
            if sprites[i].distance(sprites[j]) < COLLISION_RADIUS:
                # collision
                opp_sign = sprites[j].sign
                match sprites[i].sign:
                    case 'rock':
                        if opp_sign == 'paper':
                            sprites[i].hideturtle()
                            indices.append(i) 
                        elif opp_sign == 'scissor':
                            sprites[j].hideturtle()
                            indices.append(j) 
                    case 'paper':
                        if opp_sign == 'rock':
                            sprites[j].hideturtle()
                            indices.append(j) 
                        elif opp_sign == 'scissor':
                            sprites[i].hideturtle()
                            indices.append(i) 
                    case 'scissor':
                        if opp_sign == 'rock':
                            sprites[i].hideturtle()
                            indices.append(i) 
                        elif opp_sign == 'paper':
                            sprites[j].hideturtle()
                            indices.append(j) 
    # remove sprites that got eliminated altogether
    for idx in indices:
        sprites.pop(idx)

# buttons
start_stop_button = ControlButton('Start', 'square', 2, 3, 'purple', SS_BUTTON_X, SS_BUTTON_Y, SS_BUTTON_TEXT_Y, onStartStopToggle)
pause_resume_button = ControlButton('Pause', 'square', 2, 3, '#624a2e', PR_BUTTON_X, PR_BUTTON_Y, PR_BUTTON_TEXT_Y, onPauseResumeToggle)

rock_button = Button('circle', SUMMON_BTN_SIZE, SUMMON_BTN_SIZE, 'red', ROCK_BTN_X, SUMMON_BTN_Y, summon_rock)
paper_button = Button('square', SUMMON_BTN_SIZE, SUMMON_BTN_SIZE, 'green', PAPER_BTN_X, SUMMON_BTN_Y, summon_paper)
scissor_button = Button('triangle', SUMMON_BTN_SIZE, SUMMON_BTN_SIZE, 'blue', SCISSOR_BTN_X, SUMMON_BTN_Y, summon_scissor)

undo_button = ReverseButton('arrow', 1, 2, 'grey', UNDO_BTN_X, UNDO_BTN_Y, onUndoClick, 180, 5)
redo_button = ReverseButton('arrow', 1, 2, 'grey', REDO_BTN_X, REDO_BTN_Y, onRedoClick, 0, 5)


# game loop
while True:
    wn.update()

    for sprite in sprites:
        sprite.setx(sprite.xcor() + sprite.dx)
        sprite.sety(sprite.ycor() + sprite.dy)
        # check borders
        if sprite.xcor() > RIGHT_BORDER:
            sprite.setx(RIGHT_BORDER)
            sprite.dx *= -1
        elif sprite.xcor() < LEFT_BORDER:
            sprite.setx(LEFT_BORDER)
            sprite.dx *= -1
        if sprite.ycor() > TOP_BORDER:
            sprite.sety(TOP_BORDER)
            sprite.dy *= -1
        elif sprite.ycor() < BOTTOM_BORDER:
            sprite.sety(BOTTOM_BORDER)
            sprite.dy *= -1
    
    detectCollision()
    
    if len(sprites) < 1 or start_stop_button.toggle:
        undo_button.color('grey')
    else:
        undo_button.color('black')

    if len(copy) < 1 or start_stop_button.toggle:
        redo_button.color('grey')
    else:
        redo_button.color('black')
    
    # game over
    if start_stop_button.toggle and (len(sprites) == 1 or all(b.sign == sprites[0].sign for b in sprites)):
        for sprite in sprites:
            sprite.dx = 0
            sprite.dy = 0
        message.gameOver()


'''
TODO:
- Restart button when GAME OVER

- Ideas: when sprite eats another, it gets BIGGER and FASTER
'''