import pynput, time
from pynput import mouse, keyboard
from pynput.mouse import Button, Controller

bicep_threshold = 90
lean_threshold = 90

mouse = Controller()


def sleep():
    # gives time to switch between VSCode and minecraft executable
    time.sleep(5)

# have a sleep command called to give time for us to switch from program to 
# minecraft game
# if some input value range, do said action

def game_actions(data):
    if (data.bicep_flex > bicep_threshold):
        hit()
    if (data.lean_forward > lean_threshold):
        # walk()
    # ...


# pickaxe, hit
# pretend you equipment case has a pickaxe in the first slot, sword in second slot, 
def hit():
    mouse.press(Button.left)

def continual_hit():
    for i in range(len(5)):
        mouse.press(Button.left)


sleep()
hit()
continual_hit()

# to rotate Character in MineCraft, use mouse.move(int x, int y) or mouse.position(int x, int y). Move is more dynamic tbh 
# to switch items in your equipment handbar, use mouse.scroll(int x) where x is some number

