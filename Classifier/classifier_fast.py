# test program to determine smart weapon output

# imports
import numpy as np 
import cv2 
import pyautogui 
import time
from roboflow import Roboflow

# roboflow load model
rf = Roboflow(api_key="c5Ak0Ld4PWZ1PNR0nt23")
mob_project = rf.workspace().project("minecraft-mob-detection")
mob_model = mob_project.version(10).model

tree_project = rf.workspace().project("minecraft-tree-detection")
tree_model = tree_project.version(1).model

#counter
count = 0

def take_screenshot():
    # take screenshot using pyautogui 
    image = np.array(pyautogui.screenshot())
    
    # image formatting
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # return
    return image[340:7400, 710:1210, :]

def weapon_classifier(image):
    # visualize your prediction
    mobs = mob_model.predict(image, confidence=40, overlap=20).json().get('predictions')

    trees = tree_model.predict(image, confidence=40, overlap=20).json().get('predictions')

    for dict in trees:
        if(int(dict.get('x')) > 50 and int(dict.get('x') < 300) and int(dict.get('width')) > 50 and int(dict.get('height')) > 100):
            return 3

    for dict in mobs:
        # if the mob is in the middle of the screen AND has a reasonable size
        if(int(dict.get('x')) > 100 and int(dict.get('x') < 300) and int(dict.get('width')) > 50 and int(dict.get('height')) > 50):
            return 2

    return 1

while(1):
    weapon_classifier(take_screenshot())
    count += 1

    if(count >= 20):
        break