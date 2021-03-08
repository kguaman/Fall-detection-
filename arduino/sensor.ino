/*
  Kelvin Fall 2020
  reading sensor data
  adafruit library was implemented to read sensor data
  link: https://github.com/adafruit/Adafruit_ICM20X
  note: if another MPU is used code would need to be adjusted
*/
#include <Adafruit_ICM20948.h>
#include <Adafruit_ICM20X.h>
#include <Adafruit_Sensor.h>
#include <Wire.h>
#include <math.h>

int LED_Non_Fall= 7; 
int LED_Fall = 8; 

Adafruit_Sensor *accel2,*accel;

const float RAD2DEG = 180.0f / PI;
const float G = 9.81; 


float accx,accy,accz;
float accx_2,accy_2,accz_2;
float gyrox,gyroy,gyroz;
float gyrox_2,gyroy_2,gyroz_2;

float mag_acc, mag_acc_2;;
float mag_gyro,mag_gyro_2;

float theta_mea,phi_mea;
float thetanew,phinew; 
float thetaold = 0;
float phiold = 0;


Adafruit_ICM20948 icm;
Adafruit_ICM20948 icm2;

void setup(void) {
  
  pinMode(LED_Non_Fall,OUTPUT); 
  pinMode(LED_Fall,OUTPUT); 
  digitalWrite(LED_Non_Fall,HIGH);
  
  Serial.begin(115200);
  icm.begin_I2C(0x69);
  icm2.begin_I2C(0x68);
 
  icm.setAccelRange(ICM20948_ACCEL_RANGE_2_G);
  icm2.setAccelRange(ICM20948_ACCEL_RANGE_2_G);
  icm2.enableAccelDLPF(true, ICM20X_ACCEL_FREQ_5_7_HZ);
  icm.enableAccelDLPF(true, ICM20X_ACCEL_FREQ_5_7_HZ);
  accel = icm2.getAccelerometerSensor();
  accel2 = icm2.getAccelerometerSensor();

  // lower the DPS gyro can capture slow rotation but fast saturation
  icm.setGyroRange(ICM20948_GYRO_RANGE_2000_DPS);
  icm2.setGyroRange(ICM20948_GYRO_RANGE_2000_DPS);
  
  icm.setGyroRateDivisor(255);
  icm2.setGyroRateDivisor(255);
}
    
void loop() {
char response = Serial.read();
  if(response == 'f' or response == 'n'){
    Serial.println(response);
    if(response == 'f'){
     digitalWrite(LED_Fall, HIGH); 
     digitalWrite(LED_Non_Fall,LOW); 
     
    }
    else{
     digitalWrite(LED_Non_Fall,HIGH); 
     digitalWrite(LED_Fall,LOW); 
      }
  }
else {
 digitalWrite(LED_Non_Fall,HIGH);
 Data(); 
  }
}
    
void Data() {
  // sensor events
  sensors_event_t accel;
  sensors_event_t gyro;
  sensors_event_t mag;
  sensors_event_t temp;
  icm.getEvent(&accel, &gyro, &temp, &mag);

  sensors_event_t accel2;
  sensors_event_t gyro2;
  sensors_event_t mag2;
  sensors_event_t temp2;
  icm2.getEvent(&accel2, &gyro2, &temp2, &mag2);

  accz = accel.acceleration.z/G; 
  accy = accel.acceleration.y/G;
  accx = accel.acceleration.x/G;
  
  accx_2 = accel2.acceleration.x/G;
  accy_2 = accel2.acceleration.y/G;
  accz_2 = accel2.acceleration.z/G;

  gyrox = gyro.gyro.x;
  gyroy = gyro.gyro.y;
  gyroz = gyro.gyro.z;
  
  gyrox_2 = gyro2.gyro.x;
  gyroy_2 = gyro2.gyro.y;
  gyroz_2 = gyro2.gyro.z;
  
  // measure angle displacement
  theta_mea = (-atan2(accx_2,accz_2))* RAD2DEG;
  phi_mea = (atan2(-accx_2,accz_2))* RAD2DEG;
  thetaold = thetanew;
  phiold = phinew ;

  phinew = .3 * phiold + .7* phi_mea; // pitch 
  thetanew = .8 * thetaold + .2 * theta_mea; // row
  
  mag_acc = sqrt(square(accz) + (square(accy)) + (square(accx)));
  mag_acc_2 = sqrt(square(accx_2) + (square(accy_2)) + (square(accz_2))); 
  mag_gyro= sqrt(square(gyrox) + (square(gyroy)) + (square(gyroz)));
  mag_gyro_2 = sqrt(square(gyrox_2) + (square(gyroy_2)) + (square(gyroz_2)));

  ///thigh 
  Serial.print(accx);
  Serial.print(",");
  Serial.print(accy);
  Serial.print(",");
  Serial.print(accz);   
  Serial.print(",");
  // chest 
  Serial.print(accx_2);
  Serial.print(",");
  Serial.print(accy_2);
  Serial.print(",");
  Serial.print(accz_2);
  Serial.print(",");  
  //thigh 
  Serial.print(gyrox);
  Serial.print(",");
  Serial.print(gyroy);
  Serial.print(",");
  Serial.print(gyroz);   
  Serial.print(",");
  // chest 
  Serial.print(gyrox_2);
  Serial.print(",");
  Serial.print(gyroy_2);
  Serial.print(",");
  Serial.print(gyroz_2);  
  Serial.print(",");
  // magnitude
  Serial.print(mag_acc);
  Serial.print(",");
  Serial.print(mag_acc_2);
  Serial.print(",");
  Serial.print(mag_gyro);
  Serial.print(",");
  Serial.print(mag_gyro_2);
  Serial.print(",");
  Serial.print(phinew);
  Serial.println();  
  delay(10);
}
