from threading import Thread
import sys
import time
from pynput.keyboard import Key, Controller
import pyautogui # better than pynput for more gradual movements
from data import GameActionData

class MinecraftController:
    flex_threshold = 150
    jump_threshold = 3000
    forward_threshold = 3000
    backward_threshold = -3000
    left_threshold = -5000
    right_threshold = -5000
    uptilt_threshold = -15000
    downtilt_threshold = 15000    
    lefttilt_threshold = -15000
    righttilt_threshold = 15000

    pressing = False
    jumping = False
    walking = [False, False, False, False]
    rotating = [False, False, False, False]
    keyboard = Controller()

    def start_hit(self):
        print("started hitting")
        pyautogui.mouseDown()

    def end_hit(self):
        print("stopped hitting")
        pyautogui.mouseUp()

    def jump(self):
        pyautogui.keyDown("space")
    
    def end_jump(self):
        pyautogui.keyUp("space")

    def select_sword():
        self.keyboard.press(Key.space)

    def select_pickaxe(self):
        pyautogui.press('1')
    
    def select_sword(self):
        pyautogui.press('2')

    def select_axe(self):
        pyautogui.press('3')
    
    def rotate_right(self):
        pyautogui.moveRel(200, 0, duration = 1)

    def rotate_left(self):
        pyautogui.moveRel(-200, 0, duration = 1)

    def check_punch_start(self, flex_value):
        if (flex_value >= self.flex_threshold and not self.pressing):
            Thread(target=self.start_hit).start()
            self.pressing = True
        if (flex_value < self.flex_threshold and self.pressing):
            Thread(target=self.end_hit).start()
            self.pressing = False

    def check_start_walk(self, y, x):
        if (y >= self.forward_threshold and self.walking[0]):
            print("here")
            Thread(pyautogui.keyDown("w")).start()
            self.walking[0] = True
        if (y <= self.backward_threshold and self.walking[1]):
            Thread(pyautogui.keyDown("s")).start()
            self.walking[1] = True        
        if (x >= self.right_threshold and self.walking[2]):
            Thread(pyautogui.keyDown("d")).start()
            self.walking[2] = True        
        if (x <= self.left_threshold and self.walking[3]):
            Thread(pyautogui.keyDown("a")).start()
            self.walking[3] = True

    def check_end_walk(self, y, x):
        if (y < self.forward_threshold and not self.walking[0]):
            Thread(pyautogui.keyUp("w")).start()
            self.walking[0] = False
        if (y > self.backward_threshold and not self.walking[1]):
            Thread(pyautogui.keyUp("s")).start()
            self.walking[1] = False        
        if (x < self.right_threshold and not self.walking[2]):
            Thread(pyautogui.keyUp("d")).start()
            self.walking[2] = False        
        if (x > self.left_threshold and not self.walking[3]):
            Thread(pyautogui.keyUp("a")).start()
            self.walking[3] = False

    def check_jump(self, jump_value):
        if (jump_value >= self.jump_threshold and not self.jumping):
            Thread(target=self.jump).start()
            jumping = True
        if (jump_value < self.jump_threshold and self.jumping):
            Thread(target=self.end_jump).start()
            jumping = False

    def game_actions(self, data: GameActionData):
        self.check_punch_start(data.flex_value)
        # self.check_jump(data.jump_value)
        # self.check_start_walk(data.y_move, data.x_move)
        # self.check_end_walk(data.y_move, data.x_move)
        self.rotate_camera(data.y_tilt, data.x_tilt)

    def select_item(self, item: int):
        if (item == 2):
            self.select_sword()
        elif (item == 3):
            self.select_axe()
        else:
            self.select_pickaxe()

    def rotate_camera(self, y, x):
        if (y <= self.uptilt_threshold):
            Thread(pyautogui.moveRel(0, -30, duration=.1)).start()
        if (y >= self.downtilt_threshold):
            Thread(pyautogui.moveRel(0, 30, duration=.1)).start()
        if (x <= self.lefttilt_threshold):
            Thread(pyautogui.moveRel(30, 0, duration=.1)).start()
        if (x >= self.righttilt_threshold):
            Thread(pyautogui.moveRel(-30, 0, duration=.1)).start()


