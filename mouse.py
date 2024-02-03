import pynput, time
from pynput import mouse, keyboard
from pynput.mouse import Button, Controller

bicep_threshold = 90
lean_threshold = 90

mouse = Controller()


def pause(x):
    time.sleep(x)

# have a sleep command called to give time for us to switch from program to 
# minecraft game
# if some input value range, do said action

def game_actions(data):
    if (data.bicep_flex > bicep_threshold):
        hit()
    if (data.lean_forward > lean_threshold):
        walk()
    # ...


# pickaxe, hit
# pretend you equipment case has a pickaxe in the first slot, sword in second slot, 
def hit():
    mouse.press(Button.left)
    pause(0.5)
    mouse.release(Button.left)

def continual_hit():
    mouse.press(Button.left)
    pause(5)
    mouse.release(Button.left)

# rotate your character right
def rotate_right():
    mouse.move(700, 0)

    # Mouse.move and mouse.position doesn't work in minecraft since mouse is glued to the center. Have to change it up for rotations.


# rotate your character left
def rotate_left():
    mouse.move(-700, 0)

# these commands differentiate between a hit action, and a multi-hit action
pause(5)
hit()
pause(5)
continual_hit()

# these commands differentiate between rotating left, and rotating right
# IMPORTANT: YOU NEED TO TURN OFF RAW_INPUT IN YOUR MINECRAFT SETTINGS BEFORE TRYING THESE COMMANDS. TO DO THAT:
'''
Press Esc -> Options -> Controls -> Mouse Settings -> Raw Input: OFF
'''
pause(5)
rotate_right()
pause(5)
rotate_left()


# to rotate Character in MineCraft, use mouse.move(int x, int y) or mouse.position(int x, int y). Move is more dynamic tbh 
# to switch items in your equipment handbar, use mouse.scroll(int x) where x is some number
# to look top left, we can do sequence for now, maybe multithread to do smooth movement with a 
# diagonal mouse movement
