void setup() {
  // Start serial communication at 9600 bps.
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    // Read the incoming byte:
    String incomingData = Serial.readStringUntil('\n');
    
    // For debugging, print the incoming data to the Serial Monitor:
    Serial.print("I received: ");
    Serial.println(incomingData);
  }
