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

# have your character to hit or dig in minecraft
def hit():
    mouse.press(Button.left)
    pause(0.5)
    mouse.release(Button.left)

# have your character do a longer hit or dig in minecraft
def continual_hit(x):
    mouse.press(Button.left)
    pause(x)
    mouse.release(Button.left)

# rotate your character right
def rotate_right():
    mouse.move(700, 0)

# rotate your character left
def rotate_left():
    mouse.move(-700, 0)

'''
Note to self and Toby: Keshav talked about an input of an angle for look_down and look_up functions, 
so if person looks slightly up (45 degrees, instead of a full 90 degrees), 
and 700 causes the y axis to look fully up, multiply 700 * 0.5. If we have angle input, we can add that as a parameter
to do the aforementioned multiplications operations
'''
# have your character look down 
def look_down():
    mouse.move(0, 700)

# have your character look up
def look_up():
    mouse.move(0, 700)

# these commands test differentiation between a hit action, and a multi-hit action. use for testing.
pause(5)
hit()
pause(5)
continual_hit(5) # number parameter represents how many seconds you want to hit or dig for

# these commands test differentiation between rotating left, and rotating right. use for testing.
# IMPORTANT: YOU NEED TO TURN OFF RAW_INPUT IN YOUR MINECRAFT SETTINGS BEFORE TRYING THESE COMMANDS. TO DO THAT:
'''
Press Esc -> Options -> Controls -> Mouse Settings -> Raw Input: OFF
'''
pause(5)
rotate_right()
pause(5)
rotate_left()

# to switch items in your equipment handbar, use mouse.scroll(int x) where x is some number based off Tim's smart action
