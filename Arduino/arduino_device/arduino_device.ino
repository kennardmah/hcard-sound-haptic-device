void setup() {
  // Start serial communication at 9600 bps.
  Serial.begin(9600);
//  pinMode(3, OUTPUT);
//  pinMode(5, OUTPUT);
//  pinMode(6, OUTPUT);
//  pinMode(9, OUTPUT);
  pinMode(10, OUTPUT);  
  pinMode(11, OUTPUT);  
}

void loop() {
  if (Serial.available() >= 2) {
    uint8_t arr[2];
    // Read serial array 
    Serial.readBytes((char*)arr, 5);
    //Control output  in range 0 - 255)
    analogWrite(10, (arr[0]));
    analogWrite(11, (arr[1]));
//    analogWrite(6, (arr[2]);
//    analogWrite(9, (arr[3]);  
//    analogWrite(11, (arr[4]);
 //   analogWrite(11, (arr[5]);
 //   analogWrite(, (arr[6]);
  }
}  
