from threading import Thread
import sys
import pynput, time
from pynput import mouse, keyboard
from pynput.mouse import Button, Controller
import pyautogui # better than pynput for more gradual movements

from data import Data

class MinecraftController:
    bicep_threshold = 90
    lean_threshold = 90
    pressing = False
    rotating = False
    walking = False
    
    def start_hit(self):
        print("started hitting")
        pyautogui.mouseDown()
        sys.exit()

    def end_hit(self):
        print("stopped hitting")
        pyautogui.mouseUp()
        sys.exit()

    def game_actions(self, data):
        if (data.bicep_flex >= self.bicep_threshold and not self.pressing):
            Thread(target=self.start_hit).start()
            self.pressing = True
        if (data.bicep_flex < self.bicep_threshold and self.pressing):
            Thread(target=self.end_hit).start()
            self.pressing = False
