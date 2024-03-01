void setup() {
  // write code
  Serial.begin(9600);
}

void loop() {
  // write code
  if (Serial.available() > 0) {
  // Read the incoming data as a string
  String data = Serial.readStringUntil('\n');
  // Debug print the received string
  Serial.print("Received: ");
  Serial.println(data);
}
}
