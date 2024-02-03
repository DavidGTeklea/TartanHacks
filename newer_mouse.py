import pyautogui # better than pynput for more gradual movements
import time

'''
IMPORTANT: YOU NEED TO TURN OFF RAW_INPUT IN YOUR MINECRAFT SETTINGS 
BEFORE TRYING THESE COMMANDS. TO DO THAT:
Press Esc -> Options -> Controls -> Mouse Settings -> Raw Input: OFF
'''

def pause(x):
    time.sleep(x)

pyautogui.FAILSAFE = False # stops this script from complaining when at edge of screen

# pyautogui.moveRel has worked better than pyautogui.moveTo tbh

# have your character look up
def look_up():
    pyautogui.moveRel(0, -300, duration = 1) # moves it to a specific point, not relative

# have your character look down 
def look_down():
    pyautogui.moveRel(0, 300, duration = 1)

# rotate your character right
def rotate_right():
    pyautogui.moveRel(200, 0, duration = 1)

# rotate your character left
def rotate_left():
    pyautogui.moveRel(-200, 0, duration = 1)

# have your character to hit in minecraft
def hit():
    pyautogui.click()
    # pause(0.5), without this pause, only clicks once

# have your character place a block in minecraft
def place_block():
    pyautogui.click(button = 'right')

def dig():
    pyautogui.mouseDown()
    

# testing calls
pause(5)
dig()
pause(2)
hit()
pause(2)
place_block()
pause(2) 
rotate_left()
pause(5)
rotate_right()
pause(5)
look_up()
pause(5)
look_down()




