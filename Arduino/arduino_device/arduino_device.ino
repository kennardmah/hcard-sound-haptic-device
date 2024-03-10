void setup() {
  // Start serial communication at 9600 bps.
  Serial.begin(9600);
  pinMode(3, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(10, OUTPUT);  
  pinMode(11, OUTPUT);  
}

//back right 11, 5
//front right 3 2
//front 5 3
//front left 6 1 
//back left 10 , 4

void loop() {
  if (Serial.available() >= 2) {
    uint8_t arr[2];
    // Read serial array 
    Serial.readBytes((char*)arr, 5);
    //Control output  in range 0 - 255)
    analogWrite(10, (arr[3]));
    analogWrite(11, (arr[4]));
    analogWrite(6, (arr[0]));
    analogWrite(5, (arr[2]));  
    analogWrite(3, (arr[1]));
  }
}  
