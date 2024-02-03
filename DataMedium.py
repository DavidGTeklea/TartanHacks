import serial
import time
import struct
from data import GameActionData, RotationData
from minecraft_controller import MinecraftController
from Classifier.classifier import take_screenshot, weapon_classifier
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
rf = Roboflow(api_key="c5Ak0Ld4PWZ1PNR0nt23")
mob_project = rf.workspace().project("minecraft-mob-detection")
mob_model = mob_project.version(10).model

tree_project = rf.workspace().project("minecraft-tree-detection")
tree_model = tree_project.version(1).model

try:
    while True:
        if ser.in_waiting > 52:
            data = ser.read(52)
            DataPackage = struct.unpack('13f', data)

            Accelerometer_Value_Head = Gyroscope_Value_Head = Accelerometer_Value_Chest = Gyroscope_Value_Chest = [0.0, 0.0, 0.0]

            EMG_Value_Bicep = DataPackage[0]
            Accelerometer_Value_Head = DataPackage[1:4]
            Gyroscope_Value_Head = DataPackage[4:7]
            Accelerometer_Value_Chest = DataPackage[7:10]
            Gyroscope_Value_Chest = DataPackage[10:]

            # print("----------------")
            print("EMG Value: " + str(EMG_Value_Bicep))
            # print("EMG Value: " + str(EMG_Value_Bicep))
            # print("Accel Head Value: " + str(Accelerometer_Value_Head[0]) + ", " + str(Accelerometer_Value_Head[1]) + ", " + str(Accelerometer_Value_Head[2]))
            # print("Gyro Head Value: " + str(Gyroscope_Value_Head[0]) + ", " + str(Gyroscope_Value_Head[1]) + ", " + str(Gyroscope_Value_Head[2]))
            # print("Accel Chest Value: " + str(Accelerometer_Value_Chest[0]) + ", " + str(Accelerometer_Value_Chest[1]) + ", " + str(Accelerometer_Value_Chest[2]))
            # print("Gyro Chest Value: " + str(Gyroscope_Value_Chest[0]) + ", " + str(Gyroscope_Value_Chest[1]) + ", " + str(Gyroscope_Value_Chest[2]))
            
            game_action_data = GameActionData(flex_value = EMG_Value_Bicep, jump_value=0)
            mc_controller.game_actions(game_action_data)

            item = weapon_classifier(take_screenshot())
            

except KeyboardInterrupt:
    ser.close()
    print("Serial connection closed.")

