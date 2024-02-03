#include <MPU6050.h>
#include <Wire.h>

MPU6050 mpu_head, mpu_chest;

// Sensors
int EMG_Pin = A0;

struct Vector3f {
  float x;
  float y;
  float z;
};

// Setup
void setup() {
  Serial.begin(9600);
  Wire.begin();
  mpu_head.initialize();
  mpu_chest.initialize();
}

// Main Loop
void loop() {
  // get bicep EMG sensor
  int EMG_Value_Bicep = analogRead(EMG_Pin);

  // get head Accelerometer/Gyroscope sensor
  int16_t Accelerometer_Value_Raw_Head[3], Gyroscope_Value_Raw_Head[3];
  mpu_head.getMotion6(&Accelerometer_Value_Raw_Head[0], &Accelerometer_Value_Raw_Head[1], &Accelerometer_Value_Raw_Head[2], &Gyroscope_Value_Raw_Head[0], &Gyroscope_Value_Raw_Head[1], &Gyroscope_Value_Raw_Head[2]);
  float Accelerometer_Value_X_Head = Accelerometer_Value_Raw_Head[0] / 16384.0;
  float Accelerometer_Value_Y_Head = Accelerometer_Value_Raw_Head[1] / 16384.0;
  float Accelerometer_Value_Z_Head = Accelerometer_Value_Raw_Head[2] / 16384.0;
  float Gyroscope_Value_X_Head = Gyroscope_Value_Raw_Head[0] / 131.0;
  float Gyroscope_Value_Y_Head = Gyroscope_Value_Raw_Head[1] / 131.0;
  float Gyroscope_Value_Z_Head = Gyroscope_Value_Raw_Head[2] / 131.0;

  // get chest Accelerometer/Gryoscope sensor
  int16_t Accelerometer_Value_Raw_Chest[3], Gyroscope_Value_Raw_Chest[3];
  mpu_head.getMotion6(&Accelerometer_Value_Raw_Chest[0], &Accelerometer_Value_Raw_Chest[1], &Accelerometer_Value_Raw_Chest[2], &Gyroscope_Value_Raw_Chest[0], &Gyroscope_Value_Raw_Chest[1], &Gyroscope_Value_Raw_Chest[2]);
  float Accelerometer_Value_X_Chest = Accelerometer_Value_Raw_Chest[0] / 16384.0;
  float Accelerometer_Value_Y_Chest = Accelerometer_Value_Raw_Chest[1] / 16384.0;
  float Accelerometer_Value_Z_Chest = Accelerometer_Value_Raw_Chest[2] / 16384.0;
  float Gyroscope_Value_X_Chest = Gyroscope_Value_Raw_Chest[0] / 131.0;
  float Gyroscope_Value_Y_Chest = Gyroscope_Value_Raw_Chest[1] / 131.0;
  float Gyroscope_Value_Z_Chest = Gyroscope_Value_Raw_Chest[2] / 131.0;
  
  // send packaged data serially to python
  Serial.print(PackageData(EMG_Value_Bicep, Accelerometer_Value_X_Head, Accelerometer_Value_Y_Head, Accelerometer_Value_Z_Head, Gyroscope_Value_X_Head, Gyroscope_Value_Y_Head, Gyroscope_Value_Z_Head, Accelerometer_Value_X_Chest, Accelerometer_Value_Y_Chest, Accelerometer_Value_Z_Chest, Gyroscope_Value_X_Chest, Gyroscope_Value_Y_Chest, Gyroscope_Value_Z_Chest));
  Serial.println();
  delay(1000);
}

// Packages data into a string
String PackageData(int EMG_Value_Bicep, float Accelerometer_Value_X_Head, float Accelerometer_Value_Y_Head, float Accelerometer_Value_Z_Head, float Gyroscope_Value_X_Head, float Gyroscope_Value_Y_Head, float Gyroscope_Value_Z_Head, float Accelerometer_Value_X_Chest, float Accelerometer_Value_Y_Chest, float Accelerometer_Value_Z_Chest, float Gyroscope_Value_X_Chest, float Gyroscope_Value_Y_Chest, float Gyroscope_Value_Z_Chest){
  return String(EMG_Value_Bicep) + "," + String(Accelerometer_Value_X_Head) + "," + String(Accelerometer_Value_Y_Head) + "," + String(Accelerometer_Value_Z_Head) + "," + String(Gyroscope_Value_X_Head) + "," + String(Gyroscope_Value_Y_Head) + "," + String(Gyroscope_Value_Z_Head) + "," + String(Accelerometer_Value_X_Chest) + "," + String(Accelerometer_Value_Y_Chest) + "," + String(Accelerometer_Value_Z_Chest) + "," + String(Gyroscope_Value_X_Chest) + "," + String(Gyroscope_Value_Y_Chest) + "," + String(Gyroscope_Value_Z_Chest);
}

