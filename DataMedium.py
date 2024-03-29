import serial
import time
import struct
from data import GameActionData
from minecraft_controller import MinecraftController
from Classifier.classifier_fast import take_screenshot, weapon_classifier
from roboflow import Roboflow

# data connection to arduino
ser = serial.Serial('COM5', 9600, timeout=1)

mc_controller = MinecraftController()

time.sleep(3)
print("starting controller...")

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
            print("Gyro Chest Value: " + str(Gyroscope_Value_Chest[0]) + ", " + str(Gyroscope_Value_Chest[1]) + ", " + str(Gyroscope_Value_Chest[2]))
            
            game_action_data = GameActionData(flex_value = EMG_Value_Bicep, jump_value = Gyroscope_Value_Chest[0], y_move= Gyroscope_Value_Chest[1], x_move= Gyroscope_Value_Chest[2], y_tilt=Gyroscope_Value_Head[1], x_tilt=Gyroscope_Value_Head[2])
            mc_controller.game_actions(game_action_data)

            item = weapon_classifier(take_screenshot())
            mc_controller.select_item(item)

except KeyboardInterrupt:
    ser.close()
    print("Serial connection closed.")