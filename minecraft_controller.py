from threading import Thread
import sys
import time
from pynput.keyboard import Key, Controller
import pyautogui # better than pynput for more gradual movements
from data import GameActionData, RotationData

class MinecraftController:
    flex_threshold = 90
    jump_threshold = 90

    pressing = False
    keyboard = Controller()
    

    def start_hit(self):
        print("started hitting")
        pyautogui.mouseDown()
        sys.exit()

    def end_hit(self):
        print("stopped hitting")
        pyautogui.mouseUp()
        sys.exit()

    def jump(self):
        print("started hitting")
        self.keyboard.press(Key.space)
        sys.exit()

    def game_actions(self, data: GameActionData):
        if (data.flex_value >= self.flex_threshold and not self.pressing):
            Thread(target=self.start_hit).start()
            self.pressing = True
        if (data.flex_value < self.flex_threshold and self.pressing):
            Thread(target=self.end_hit).start()
            self.pressing = False
        if (data.jump_value >= self.jump_threshold):
            Thread(target=self.jump).start()

    def rotate_camera(self, data: RotationData):
        y_value = data.x_value / 10
        x_value = data.y_value / 10
        pyautogui.moveRel(200 * x_value, 300 * y_value, duration=1)


