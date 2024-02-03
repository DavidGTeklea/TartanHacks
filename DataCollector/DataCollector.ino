#include <MPU6050.h>
#include <Wire.h>


// Sensors
int EMG_Pin = A0;

const int mpu_chest = 0x69, mpu_head = 0x68;

int16_t Accelerometer_Value_X_Head, Accelerometer_Value_Y_Head, Accelerometer_Value_Z_Head, Gyroscope_Value_X_Head, Gyroscope_Value_Y_Head, Gyroscope_Value_Z_Head, Accelerometer_Value_X_Chest, Accelerometer_Value_Y_Chest, Accelerometer_Value_Z_Chest, Gyroscope_Value_X_Chest, Gyroscope_Value_Y_Chest, Gyroscope_Value_Z_Chest;
int16_t Temp1, Temp2;

// Setup
void setup() {
  Wire.begin();
  Wire.beginTransmission(mpu_head);
  Wire.write(0x6B);
  Wire.write(0);
  Wire.endTransmission(true);
  
  Wire.begin();
  Wire.beginTransmission(mpu_chest);
  Wire.write(0x6B);
  Wire.write(0);
  Wire.endTransmission(true);

  Serial.begin(9600);

}

// Main Loop
void loop() {
  // get bicep EMG sensor
  int16_t EMG_Value_Bicep = analogRead(EMG_Pin);

  // get head Accelerometer/Gyroscope sensor
  GetMPUHead(mpu_head);
  
  // get chest Accelerometer/Gryoscope sensor
  GetMPUChest(mpu_chest);
  
  // send packaged data serially to python
  float DataPackage[]= {EMG_Value_Bicep, Accelerometer_Value_X_Head, Accelerometer_Value_Y_Head, Accelerometer_Value_Z_Head, Gyroscope_Value_X_Head, Gyroscope_Value_Y_Head, Gyroscope_Value_Z_Head, Accelerometer_Value_X_Chest, Accelerometer_Value_Y_Chest, Accelerometer_Value_Z_Chest, Gyroscope_Value_X_Chest, Gyroscope_Value_Y_Chest, Gyroscope_Value_Z_Chest};
  Serial.write((uint8_t*)DataPackage, sizeof(DataPackage));
  delay(1000);
}

void GetMPUHead(const int MPU){ 
  Wire.beginTransmission(MPU); 
  Wire.write(0x3B); 
  Wire.endTransmission(false);
  Wire.requestFrom(MPU, 14, true);
  Accelerometer_Value_X_Head = Wire.read()<<8| Wire.read();
  Accelerometer_Value_Y_Head = Wire.read()<<8|  Wire.read();
  Accelerometer_Value_Z_Head = Wire.read()<<8| Wire.read();
  Temp1 = Wire.read()<<8| Wire.read();
  Gyroscope_Value_X_Head = Wire.read()<<8| Wire.read();
  Gyroscope_Value_Y_Head = Wire.read()<<8| Wire.read();
  Gyroscope_Value_Z_Head = Wire.read()<<8| Wire.read();
}
     
void GetMPUChest(const int MPU){ 
  Wire.beginTransmission(MPU); 
  Wire.write(0x3B); 
  Wire.endTransmission(false);
  Wire.requestFrom(MPU, 14, true);
  Accelerometer_Value_X_Chest = Wire.read()<<8| Wire.read();
  Accelerometer_Value_Y_Chest = Wire.read()<<8|  Wire.read();
  Accelerometer_Value_Z_Chest = Wire.read()<<8| Wire.read();
  Temp2 = Wire.read()<<8| Wire.read();
  Gyroscope_Value_X_Chest = Wire.read()<<8| Wire.read();
  Gyroscope_Value_Y_Chest = Wire.read()<<8| Wire.read();
  Gyroscope_Value_Z_Chest = Wire.read()<<8| Wire.read();
}

