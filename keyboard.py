import pynput, time
from pynput.keyboard import Key, Controller

keyboard = Controller()

def just_for_testing():
    time.sleep(5)

def jump():
    keyboard.press(Key.space)

def walk():
    keyboard.press('w')
    for i in range(10):
        if i > 8:
            stopWalk()


def stopWalk():
    keyboard.release('w')

just_for_testing()

walk()    

jump()

