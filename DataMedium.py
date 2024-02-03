import serial
import time
import struct
from data import GameActionData
from minecraft_controller import MinecraftController
from Classifier.classifier_fast import take_screenshot, weapon_classifier
from roboflow import Roboflow

# data connection to arduino
ser = serial.Serial('COM5', 9600, timeout=1)

# default sensor values
EMG_Value_Default_Bicep = 90.0
Accelerometer_Value_Default_Head = [-2000.0, -1000.0, 18000.0]
# Look up/down: up = [2500, -, -], down = [-, -, 10000]
# Look left/right: left = [2500, -, -], right = [-, 2500, -]
Gyroscope_Value_Default_Head = [-6000.0, -9000.0, 11500.0]
Accelerometer_Value_Default_Chest = [-1100.0, 18000.0, -1000.0]
Gyroscope_Value_Default_Chest= [100.0, -9000.0, 11500.0]

mc_controller = MinecraftController()

try:
    while True:
        item = weapon_classifier(take_screenshot())
        mc_controller.select_item(item)

except KeyboardInterrupt:
    print("Serial connection closed.")