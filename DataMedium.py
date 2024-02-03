import serial
import time

ser = serial.Serial('/dev/cu.usbmodem101', 9600, timeout=1)

# Signals to Minecraft Handler
AttackSignal = 0
JumpSignal = 0
ForwardBackwardSignal = 0

try:
    while True:
        if ser.in_waiting > 0:
            data = ser.readline().decode('utf-8').rstrip()
            Accelerometer_Value_Head = Gyroscope_Value_Head = Accelerometer_Value_Chest = Gyroscope_Value_Chest = [0.0, 0.0, 0.0]
            sensor_values = [float(value) for value in data.split(",")]
            EMG_Value_Bicep, Accelerometer_Value_Head[0], Accelerometer_Value_Head[1], Accelerometer_Value_Head[2], Gyroscope_Value_Head[0], Gyroscope_Value_Head[1], Gyroscope_Value_Head[2], Accelerometer_Value_Chest[0], Accelerometer_Value_Chest[1], Accelerometer_Value_Chest[2], Gyroscope_Value_Chest[0], Gyroscope_Value_Chest[1], Gyroscope_Value_Chest[2] = sensor_values

except KeyboardInterrupt:
    ser.close()
    print("Serial connection closed.")

