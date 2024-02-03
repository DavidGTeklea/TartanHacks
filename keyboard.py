import pynput, time
from pynput.keyboard import Key, Controller

keyboard = Controller()

def just_for_testing():
    time.sleep(5)

def jump():
    keyboard.press(Key.space)
    keyboard.release(Key.space)

def walk():
    keyboard.press('w')

just_for_testing()
jump()
jump()
jump()

for i in range(10):
    walk()


