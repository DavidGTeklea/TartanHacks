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
    walking = [False, False, False, False]
    keyboard = Controller()

    def start_hit(self):
        print("started hitting")
        pyautogui.mouseDown()

    def end_hit(self):
        print("stopped hitting")
        pyautogui.mouseUp()

    def jump(self):
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

    def check_start_walk(self, forward, backward, left, right):
        if (forward >= self.forward_threshold and self.walking[0]):
            Thread(self.keyboard.press('w')).start()
            self.walking[0] = True
        if (backward <= self.backward_threshold and self.walking[1]):
            Thread(self.keyboard.press('s')).start()
            self.walking[1] = True        
        if (right >= self.right_threshold and self.walking[2]):
            Thread(self.keyboard.press('d')).start()
            self.walking[2] = True        
        if (left <= self.left_threshold and self.walking[3]):
            Thread(self.keyboard.press('a')).start()
            self.walking[3] = True

    def check_end_walk(self, forward, backward, left, right):
        if (forward < self.forward_threshold and not self.walking[0]):
            Thread(self.keyboard.release('w')).start()
            self.walking[0] = False
        if (backward > self.backward_threshold and not self.walking[1]):
            Thread(self.keyboard.release('s')).start()
            self.walking[1] = False        
        if (right < self.right_threshold and not self.walking[2]):
            Thread(self.keyboard.release('d')).start()
            self.walking[2] = False        
        if (left > self.left_threshold and not self.walking[3]):
            Thread(self.keyboard.release('a')).start()
            self.walking[3] = False

    def check_jump(self, jump_value):
        if (jump_value >= self.jump_threshold):
            Thread(target=self.jump).start()

    def game_actions(self, data: GameActionData):
        self.check_punch_start(data.flex_value)
        self.check_start_walk(data.forward_value, data.backward_value, data.left_value, data.right_value)
        self.check_end_walk(data.forward_value, data.backward_value, data.left_value, data.right_value)
        self.rotate_camera(data.tiltup_value, data.tiltdown_value, data.tiltleft_value, data.tiltright_value)

    def select_item(self, item: int):
        if (item == 2):
            self.select_sword()
        elif (item == 3):
            self.select_axe()
        else:
            self.select_pickaxe()

    def rotate_camera(self, tiltup_value, tiltdown_value, tiltleft_value, tiltright_value):
        if (tiltup_value <= self.uptilt_threshold):
            Thread(pyautogui.moveRel(0, 30, duration=1)).start()
        if (tiltdown_value >= self.downtilt_threshold):
            Thread(pyautogui.moveRel(0, -30, duration=1)).start()
        if (tiltleft_value <= self.lefttilt_threshold):
            Thread(pyautogui.moveRel(20, 0, duration=1)).start()
        if (tiltright_value >= self.righttilt_threshold):
            Thread(pyautogui.moveRel(-20, 0, duration=1)).start()

