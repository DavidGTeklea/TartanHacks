import serial
import time
import struct

ser = serial.Serial('/dev/cu.usbmodem1101', 9600, timeout=1)

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

            print("----------------")
            print("EMG Value: " + str(EMG_Value_Bicep))
            print("Accel Head Value: " + str(Accelerometer_Value_Head[0]) + ", " + str(Accelerometer_Value_Head[1]) + ", " + str(Accelerometer_Value_Head[2]))
            print("Gyro Head Value: " + str(Gyroscope_Value_Head[0]) + ", " + str(Gyroscope_Value_Head[1]) + ", " + str(Gyroscope_Value_Head[2]))
            print("Accel Chest Value: " + str(Accelerometer_Value_Chest[0]) + ", " + str(Accelerometer_Value_Chest[1]) + ", " + str(Accelerometer_Value_Chest[2]))
            print("Gyro Chest Value: " + str(Gyroscope_Value_Chest[0]) + ", " + str(Gyroscope_Value_Chest[1]) + ", " + str(Gyroscope_Value_Chest[2]))

except KeyboardInterrupt:
    ser.close()
    print("Serial connection closed.")

