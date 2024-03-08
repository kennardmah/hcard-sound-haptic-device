int buttonPin = 13;
int BackRight_1 = 11;
int FrontRight_2 = 3;
int Front_3 = 5;
int FrontLeft_4 = 6;
int BackLeft_5 = 10;

void setup() {
  // put your setup code here, to run once:
  // Start serial communication at 9600 bps.
  pinMode(3, OUTPUT);
  pinMode(5, OUTPUT);
  pinMode(6, OUTPUT);
  pinMode(10, OUTPUT);  
  pinMode(11, OUTPUT);  
}

void loop() {
  // put your main code here, to run repeatedly:
  int buttonState = digitalRead(buttonPin);

  // Control output in range 0 - 255
  if (buttonState == HIGH) {
    // Turn motors on:
    // analogWrite(3,0);
    // analogWrite(5,0);
    // analogWrite(6,100);
    // analogWrite(10,0);
    // analogWrite(11,0);
    // delay(5000);

    // Loop through each motor
    analogWrite(11,100);
    delay(1000);
    analogWrite(11,0);
    analogWrite(3,100);
    delay(1000);
    analogWrite(3,0);
    analogWrite(5,100);
    delay(1000);
    analogWrite(5,0);
    analogWrite(6,100);
    delay(1000);
    analogWrite(6,0);
    analogWrite(10,100);
    delay(1000);
    analogWrite(10,0);

    // analogWrite(3,25);
    // analogWrite(5,25);
    // analogWrite(6,25);
    // delay(2000);
    // analogWrite(3,0);
    // analogWrite(5,0);
    // analogWrite(6,0);
    // analogWrite(10,25);
    // analogWrite(11,25);
    // delay(2000);
    // analogWrite(10,0);
    // analogWrite(11,0);
    // analogWrite(3,25);
    // analogWrite(5,25);
    // analogWrite(6,25);
    // delay(2000);
    // analogWrite(3,0);
    // analogWrite(5,0);
    // analogWrite(6,0);
    // analogWrite(10,25);
    // analogWrite(11,25);
    // delay(2000);
    // analogWrite(10,0);
    // analogWrite(11,0);

  } else {
    // Turn motors off:
    analogWrite(3,0);
    analogWrite(5,0);
    analogWrite(6,0);
    analogWrite(10,0);
    analogWrite(11,0);
  }
}
