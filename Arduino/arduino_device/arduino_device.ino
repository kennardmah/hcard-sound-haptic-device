void setup() {
  // Start serial communication at 9600 bps.
  Serial.begin(9600);
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
}

void loop() {
  if (Serial.available() >= 2) {
    uint8_t arr[2];
    Serial.readBytes((char*)arr, 2);
//    int incomingInt = Serial.parseInt();
    digitalWrite(10, (arr[0]>30));
    digitalWrite(11, (arr[1]>30));
//    // Debug to check if received
//    if (arr[0]> 30){
//      digitalWrite(10, LOW);
//      digitalWrite(11, LOW);
//    }
//    else if (incomingInt == 1){
//      digitalWrite(10, LOW);
//      digitalWrite(11, HIGH);
//    }
//    else if (incomingInt == 2){
//      digitalWrite(10, HIGH);
//      digitalWrite(11, LOW);
//    }
//    else{
//      digitalWrite(11, HIGH);
//      digitalWrite(10, HIGH);
//    }
//    
  }
}
