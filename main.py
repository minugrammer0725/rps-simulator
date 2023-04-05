from turtle import Screen
from random import randint

from separator import Separator
from message import Message
from sprite import Sprite
from buttons import Button, ControlButton, ReverseButton, RestartButton

# Constants
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

SEPARATOR_X = 200
SEPARATOR_Y = 300

MESSAGE_TIMEOUT = 1700
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

RE_BTN_X = -150
RE_BTN_Y = 80
RE_BTN_TEXT_Y = 100


# all sprites on the screen
sprites = []
# copy array used for undo/redo
copy = []
# intial dx, dy values
options = [INIT_SPEED, -INIT_SPEED]

# helper functions
def canStart():
    if len(sprites) < 2 or notEnoughUniqueItems():
        return False
    return True

def notEnoughUniqueItems():
    sign = sprites[0].getSign()
    count = 0
    for sprite in sprites:
        if sign == sprite.getSign():
            count += 1
    return True if count == len(sprites)  else False

def moveSprites():
    for sprite in sprites:
        sprite.moveSprite()
        sprite.checkBorders(TOP_BORDER, BOTTOM_BORDER, RIGHT_BORDER, LEFT_BORDER)

def checkUndoRedo():
    if len(sprites) < 1 or start_stop_button.isActive():
        undo_button.setColor('grey')
    else:
        undo_button.setColor('black')

    if len(copy) < 1 or start_stop_button.isActive():
        redo_button.setColor('grey')
    else:
        redo_button.setColor('black')

def isGameOver():
    if start_stop_button.isActive() and (len(sprites) == 1 or all(b.getSign() == sprites[0].getSign() for b in sprites)):
        for sprite in sprites:
            sprite.setDx(0)
            sprite.setDy(0)
        message.gameOver()
        restart_button.restart()

# click events
def onWindowClick(x, y):
    # if (x, y) is within board borders, summon a sprite
    if not(LEFT_BORDER<= x <=RIGHT_BORDER and BOTTOM_BORDER <= y <= TOP_BORDER and not start_stop_button.isActive()):
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


def onStartStopToggle(x, y):
    if not canStart():
        message.writeMessage('Summon at least 2 different items', wn, MESSAGE_TIMEOUT)
        return
    
    start_stop_button.clearPen(SS_BUTTON_X, SS_BUTTON_TEXT_Y)
    if start_stop_button.isActive():
        start_stop_button.updateLabel('Start')
        for sprite in sprites:
            sprite.hideSprite()
        sprites.clear()
        # after game has stopped, the pause/resume button should be on pause.
        pause_resume_button.resetToPause(PR_BUTTON_X, PR_BUTTON_Y, PR_BUTTON_TEXT_Y)

    else:
        message.clearMessage()
        start_stop_button.updateLabel('Stop')
        for sprite in sprites:
            sprite.setDx(options[randint(0,1)])
            sprite.setDy(options[randint(0,1)])
    start_stop_button.moveButton(SS_BUTTON_X, SS_BUTTON_Y)
    start_stop_button.toggleStatus()
    # reset summon buttons
    wn.selected = None
    rock_button.setSize(SUMMON_BTN_SIZE, SUMMON_BTN_SIZE)
    paper_button.setSize(SUMMON_BTN_SIZE, SUMMON_BTN_SIZE)
    scissor_button.setSize(SUMMON_BTN_SIZE, SUMMON_BTN_SIZE)
    # empty copy array
    copy.clear()

def onPauseResumeToggle(x, y):
    if not start_stop_button.isActive():
        message.writeMessage('Game has not started yet', wn, MESSAGE_TIMEOUT)
        return
    pause_resume_button.clearPen(PR_BUTTON_X, PR_BUTTON_TEXT_Y)
    if pause_resume_button.isActive():
        pause_resume_button.updateLabel('Pause')
        for sprite in sprites:
            sprite.setDx(sprite.getPrevDx())
            sprite.setDy(sprite.getPrevDy())
    else:
        pause_resume_button.updateLabel('Resume')
        for sprite in sprites:
            sprite.setPrevDx(sprite.getDx())
            sprite.setPrevDy(sprite.getDy())
            sprite.setDx(0)
            sprite.setDy(0)
    pause_resume_button.moveButton(PR_BUTTON_X, PR_BUTTON_Y)
    pause_resume_button.toggleStatus()

def summon_rock(x, y):
    if start_stop_button.isActive():
        return
    wn.selected = 'rock'
    rock_button.setSize(SUMMON_BTN_HOVER, SUMMON_BTN_HOVER)
    paper_button.setSize(SUMMON_BTN_SIZE,SUMMON_BTN_SIZE)
    scissor_button.setSize(SUMMON_BTN_SIZE, SUMMON_BTN_SIZE)

def summon_paper(x, y):
    if start_stop_button.isActive():
        return
    wn.selected = 'paper'
    rock_button.setSize(SUMMON_BTN_SIZE, SUMMON_BTN_SIZE)
    paper_button.setSize(SUMMON_BTN_HOVER,SUMMON_BTN_HOVER)
    scissor_button.setSize(SUMMON_BTN_SIZE, SUMMON_BTN_SIZE)

def summon_scissor(x, y):
    if start_stop_button.isActive():
        return
    wn.selected = 'scissor'
    rock_button.setSize(SUMMON_BTN_SIZE, SUMMON_BTN_SIZE)
    paper_button.setSize(SUMMON_BTN_SIZE,SUMMON_BTN_SIZE)
    scissor_button.setSize(SUMMON_BTN_HOVER, SUMMON_BTN_HOVER)


def onUndoClick(x, y):
    # check if data arr is non-empty
    if start_stop_button.isActive():
        return 
    if len(sprites) < 1:
        message.writeMessage('Cannot Undo', wn, MESSAGE_TIMEOUT)
        return
    sprite = sprites.pop()
    sprite.hideSprite()
    copy.append(sprite)
     

def onRedoClick(x, y):
    # check if copy arr is non-empty
    if start_stop_button.isActive():
        return 
    if len(copy) < 1:
        message.writeMessage('Cannot Redo', wn, MESSAGE_TIMEOUT)
        return
    sprite = copy.pop()
    sprite.showSprite()
    sprites.append(sprite)

def onRestart(x, y):
    for sprite in sprites:
        sprite.hideSprite()
    sprites.clear()
    copy.clear()

    start_stop_button.toggleStatus()
    restart_button.removeButton()


    
# collision detection
def detectCollision():
    indices = []
    for i in range(len(sprites)):
        for j in range(i+1, len(sprites)):
            if sprites[i].distance(sprites[j]) < COLLISION_RADIUS:
                opp_sign = sprites[j].getSign()
                match sprites[i].getSign():
                    case 'rock':
                        if opp_sign == 'paper':
                            sprites[i].hideSprite()
                            indices.append(i) 
                        elif opp_sign == 'scissor':
                            sprites[j].hideSprite()
                            indices.append(j) 
                    case 'paper':
                        if opp_sign == 'rock':
                            sprites[j].hideSprite()
                            indices.append(j) 
                        elif opp_sign == 'scissor':
                            sprites[i].hideSprite()
                            indices.append(i) 
                    case 'scissor':
                        if opp_sign == 'rock':
                            sprites[i].hideSprite()
                            indices.append(i) 
                        elif opp_sign == 'paper':
                            sprites[j].hideSprite()
                            indices.append(j) 
    # remove sprites that got eliminated altogether
    for idx in indices:
        sprites.pop(idx)


# singleton window object
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

# buttons
start_stop_button = ControlButton('Start', 'square', 2, 3, 'purple', SS_BUTTON_X, SS_BUTTON_Y, SS_BUTTON_TEXT_Y, onStartStopToggle)
pause_resume_button = ControlButton('Pause', 'square', 2, 3, '#624a2e', PR_BUTTON_X, PR_BUTTON_Y, PR_BUTTON_TEXT_Y, onPauseResumeToggle)

rock_button = Button('circle', SUMMON_BTN_SIZE, SUMMON_BTN_SIZE, 'red', ROCK_BTN_X, SUMMON_BTN_Y, summon_rock)
paper_button = Button('square', SUMMON_BTN_SIZE, SUMMON_BTN_SIZE, 'green', PAPER_BTN_X, SUMMON_BTN_Y, summon_paper)
scissor_button = Button('triangle', SUMMON_BTN_SIZE, SUMMON_BTN_SIZE, 'blue', SCISSOR_BTN_X, SUMMON_BTN_Y, summon_scissor)

undo_button = ReverseButton('arrow', 1, 2, 'grey', UNDO_BTN_X, UNDO_BTN_Y, onUndoClick, 180, 5)
redo_button = ReverseButton('arrow', 1, 2, 'grey', REDO_BTN_X, REDO_BTN_Y, onRedoClick, 0, 5)

restart_button = RestartButton('Restart', 'square', 2, 3, 'gold', RE_BTN_X, RE_BTN_Y, RE_BTN_TEXT_Y, onRestart)

# game loop
while True:
    wn.update()

    moveSprites()
    
    detectCollision()
    
    checkUndoRedo()
    
    isGameOver()


'''
TODO:
- Restart button when GAME OVER

- Ideas: when sprite eats another, it gets BIGGER and FASTER
'''