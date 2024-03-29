int BackRight_1 = 6;
int FrontRight_2 = 5;
int Front_3 = 3;
int FrontLeft_4 = 10;
int BackLeft_5 = 11;
int power = 120;

void setup() {
  Serial.begin(9600);
  pinMode(BackRight_1, OUTPUT);
  pinMode(FrontRight_2, OUTPUT);
  pinMode(Front_3, OUTPUT);
  pinMode(FrontLeft_4, OUTPUT);
  pinMode(BackLeft_5, OUTPUT); 
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();

    // Turn ALL motors ON
    if (command == 't') {
      analogWrite(BackRight_1,power);
      analogWrite(FrontRight_2,power);
      analogWrite(Front_3,power);
      analogWrite(FrontLeft_4,power);
      analogWrite(BackLeft_5,power);
      delay(3000);
      analogWrite(BackRight_1,0);
      analogWrite(FrontRight_2,0);
      analogWrite(Front_3,0);
      analogWrite(FrontLeft_4,0);
      analogWrite(BackLeft_5,0);

    // Loop through each motor
    } else if (command == 'l') {
      analogWrite(BackRight_1,power);
      delay(2000);
      analogWrite(BackRight_1,0);
      analogWrite(FrontRight_2,power);
      delay(2000);
      analogWrite(FrontRight_2,0);
      // analogWrite(Front_3,power);
      // delay(2000);
      // analogWrite(Front_3,0);
      analogWrite(FrontLeft_4,power);
      delay(2000);
      analogWrite(FrontLeft_4,0);
      analogWrite(BackLeft_5,power);
      delay(2000);
      analogWrite(BackLeft_5,0);

    // Alternate between motors
    } else if (command == 'm') {
      analogWrite(FrontRight_2,power);
      // analogWrite(Front_3,power);
      analogWrite(FrontLeft_4,power);
      delay(2000);
      analogWrite(FrontRight_2,0);
      // analogWrite(Front_3,0);
      analogWrite(FrontLeft_4,0);
      analogWrite(BackLeft_5,power);
      analogWrite(BackRight_1,power);
      delay(2000);
      analogWrite(BackLeft_5,0);
      analogWrite(BackRight_1,0);
      analogWrite(FrontRight_2,power);
      // analogWrite(Front_3,power);
      analogWrite(FrontLeft_4,power);
      delay(2000);
      analogWrite(FrontRight_2,0);
      // analogWrite(Front_3,0);
      analogWrite(FrontLeft_4,0);
      analogWrite(BackLeft_5,power);
      analogWrite(BackRight_1,power);
      delay(2000);
      analogWrite(BackLeft_5,0);
      analogWrite(BackRight_1,0);
    } else if (command == 'n') {
      analogWrite(FrontLeft_4,power);
      analogWrite(BackLeft_5,power);
      delay(2000);
      analogWrite(FrontLeft_4,0);
      analogWrite(BackLeft_5,0);
      analogWrite(BackRight_1,power);
      analogWrite(FrontRight_2,power);
      delay(2000);
      analogWrite(BackRight_1,0);
      analogWrite(FrontRight_2,0);
      analogWrite(FrontLeft_4,power);
      analogWrite(BackLeft_5,power);
      delay(2000);
      analogWrite(FrontLeft_4,0);
      analogWrite(BackLeft_5,0);
      analogWrite(BackRight_1,power);
      analogWrite(FrontRight_2,power);
      delay(2000);
      analogWrite(BackRight_1,0);
      analogWrite(FrontRight_2,0);

    // Turn ON individual motor
    } else if (command == '1') {
      analogWrite(BackRight_1,power);
      delay(2000);
      analogWrite(BackRight_1,0);
    } else if (command == '2') {
      analogWrite(FrontRight_2,power);
      delay(2000);
      analogWrite(FrontRight_2,0);
    } else if (command == '3') {
      analogWrite(Front_3,power);
      delay(2000);
      analogWrite(Front_3,0);
    } else if (command == '4') {
      analogWrite(FrontLeft_4,power);
      delay(2000);
      analogWrite(FrontLeft_4,0);
    } else if (command == '5') {
      analogWrite(BackLeft_5,power);
      delay(2000);
      analogWrite(BackLeft_5,0);

    // Sequences of two motors
    } else if (command == '6') {
      analogWrite(FrontLeft_4,power);
      delay(2000);
      analogWrite(FrontLeft_4,0);
      analogWrite(BackRight_1,power);
      delay(2000);
      analogWrite(BackRight_1,0);
    } else if (command == '7') {
      analogWrite(BackRight_1,power);
      delay(2000);
      analogWrite(BackRight_1,0);
      analogWrite(BackLeft_5,power);
      delay(2000);
      analogWrite(BackLeft_5,0);
    } else if (command == '8') {
      analogWrite(BackLeft_5,power);
      delay(2000);
      analogWrite(BackLeft_5,0);
      analogWrite(FrontLeft_4,power);
      delay(2000);
      analogWrite(FrontLeft_4,0);
    } else if (command == '9') {
      analogWrite(FrontRight_2,power);
      delay(2000);
      analogWrite(FrontRight_2,0);
      analogWrite(BackLeft_5,power);
      delay(2000);
      analogWrite(BackLeft_5,0);

    // Sequences of three motors  
    } else if (command == '0') {
      analogWrite(FrontLeft_4,power);
      delay(2000);
      analogWrite(FrontLeft_4,0);
      analogWrite(BackLeft_5,power);
      delay(2000);
      analogWrite(BackLeft_5,0);
      analogWrite(FrontRight_2,power);
      delay(2000);
      analogWrite(FrontRight_2,0);
    } else if (command == 'p') {
      analogWrite(FrontLeft_4,power);
      delay(2000);
      analogWrite(FrontLeft_4,0);
      analogWrite(BackRight_1,power);
      delay(2000);
      analogWrite(BackRight_1,0);
      analogWrite(BackLeft_5,power);
      delay(2000);
      analogWrite(BackLeft_5,0);

    // Challenge sequence of four motors! 
    } else if (command == 'c') {
      analogWrite(BackLeft_5,power);
      delay(2000);
      analogWrite(BackLeft_5,0);
      analogWrite(FrontLeft_4,power);
      delay(2000);
      analogWrite(FrontLeft_4,0);
      analogWrite(FrontRight_2,power);
      delay(2000);
      analogWrite(FrontRight_2,0);
      analogWrite(BackRight_1,power);
      delay(2000);
      analogWrite(BackRight_1,0);
    } else if (command == 'v') {
      analogWrite(FrontLeft_4,power);
      delay(2000);
      analogWrite(FrontLeft_4,0);
      analogWrite(BackRight_1,power);
      delay(2000);
      analogWrite(BackRight_1,0);
      analogWrite(BackLeft_5,power);
      delay(2000);
      analogWrite(BackLeft_5,0);
      analogWrite(FrontRight_2,power);
      delay(2000);
      analogWrite(FrontRight_2,0);
    }
  }
}
