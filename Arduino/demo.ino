int buttonPin = 13;
int BackRight_1 = 11;
int FrontRight_2 = 3;
int Front_3 = 5;
int FrontLeft_4 = 6;
int BackLeft_5 = 10;

void setup() {
  // put your setup code here, to run once:
  // Start serial communication at 9600 bps.
  pinMode(BackRight_1, OUTPUT);
  pinMode(FrontRight_2, OUTPUT);
  pinMode(Front_3, OUTPUT);
  pinMode(FrontLeft_4, OUTPUT);
  pinMode(BackLeft_5, OUTPUT);    
}

void loop() {
  // put your main code here, to run repeatedly:
  int buttonState = digitalRead(buttonPin);

  // Control output in range 0 - 255
  if (buttonState == HIGH) {
    // Turn motors on:
    analogWrite(BackRight_1,0);
    analogWrite(FrontRight_2,0);
    analogWrite(Front_3,0);
    analogWrite(FrontLeft_4,0);
    analogWrite(BackLeft_5,100);
    delay(5000);

    // Loop through each motor
    // analogWrite(BackRight_1,100);
    // delay(2000);
    // analogWrite(BackRight_1,0);
    // analogWrite(FrontRight_2,100);
    // delay(2000);
    // analogWrite(FrontRight_2,0);
    // analogWrite(Front_3,100);
    // delay(2000);
    // analogWrite(Front_3,0);
    // analogWrite(FrontLeft_4,100);
    // delay(2000);
    // analogWrite(FrontLeft_4,0);
    // analogWrite(BackLeft_5,100);
    // delay(2000);
    // analogWrite(BackLeft_5,0);

    // Alternate between front and back motors
    // analogWrite(FrontRight_2,25);
    // analogWrite(Front_3,25);
    // analogWrite(FrontLeft_4,25);
    // delay(2000);
    // analogWrite(FrontRight_2,0);
    // analogWrite(Front_3,0);
    // analogWrite(FrontLeft_4,0);
    // analogWrite(BackLeft_5,25);
    // analogWrite(BackRight_1,25);
    // delay(2000);
    // analogWrite(BackLeft_5,0);
    // analogWrite(BackRight_1,0);
    // analogWrite(FrontRight_2,25);
    // analogWrite(Front_3,25);
    // analogWrite(FrontLeft_4,25);
    // delay(2000);
    // analogWrite(FrontRight_2,0);
    // analogWrite(Front_3,0);
    // analogWrite(FrontLeft_4,0);
    // analogWrite(BackLeft_5,25);
    // analogWrite(BackRight_1,25);
    // delay(2000);
    // analogWrite(BackLeft_5,0);
    // analogWrite(BackRight_1,0);

  } else {
    // Turn motors off:
    analogWrite(BackRight_1,0);
    analogWrite(FrontRight_2,0);
    analogWrite(Front_3,0);
    analogWrite(FrontLeft_4,0);
    analogWrite(BackLeft_5,0);
  }
}
