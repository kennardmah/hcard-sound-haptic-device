void setup() {
  // Start serial communication at 9600 bps.
  Serial.begin(9600);
  pinMode(11, OUTPUT);
  pinMode(10, OUTPUT);
}

void loop() {
  if (Serial.available() > 0) {
    // Read the incoming integer:
    int incomingInt = Serial.parseInt();
    
    // Debug to check if received
    if (incomingInt == 0){
      digitalWrite(10, LOW);
      digitalWrite(11, LOW);
    }
    else if (incomingInt == 1){
      digitalWrite(10, LOW);
      digitalWrite(11, HIGH);
    }
    else if (incomingInt == 2){
      digitalWrite(10, HIGH);
      digitalWrite(11, LOW);
    }
    else{
      digitalWrite(11, HIGH);
      digitalWrite(10, HIGH);
    }
  }
}
