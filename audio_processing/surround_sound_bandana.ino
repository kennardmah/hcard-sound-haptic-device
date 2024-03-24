#include <string.h>
int BackRight = 11;
int FrontRight = 9;
int FrontLeft = 5;
int BackLeft = 3;
uint8_t arr[6];
uint8_t prev_arr[6] = {0};

void setup() {
  // Start serial communication at 9600 bps.
  Serial.begin(500000);
  pinMode(BackRight, OUTPUT); 
  pinMode(FrontRight, OUTPUT);
  pinMode(FrontLeft, OUTPUT);
  pinMode(BackLeft, OUTPUT);   
}

void loop() {
  if (Serial.available() >= 6) {
    // Read serial array 
    Serial.readBytes((char*)arr, 6);

    // Compare new array with the previous one
    if (memcmp(prev_arr, arr, 6) != 0) { // If different
      // Control output in range 0 - 255
      analogWrite(FrontLeft, arr[0]);
      delay(1);
      analogWrite(FrontRight, arr[1]);
      delay(1);
      analogWrite(BackLeft, arr[4]);
      delay(1);
      analogWrite(BackRight, arr[5]);

      // Copy new array to prev_arr for the next loop iteration
      memcpy(prev_arr, arr, 6);
    }
  }
}  
