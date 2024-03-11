int BackRight_1 = 11;
int FrontRight_2 = 3;
int Front_3 = 5;
int FrontLeft_4 = 6;
int BackLeft_5 = 10;

void setup() {
  // Start serial communication at 9600 bps.
  Serial.begin(9600);
  pinMode(BackRight_1, OUTPUT); 
  pinMode(FrontRight_2, OUTPUT);
  pinMode(Front_3, OUTPUT);
  pinMode(FrontLeft_4, OUTPUT);
  pinMode(BackLeft_5, OUTPUT);   
}

void loop() {
  if (Serial.available() >= 2) {
    uint8_t arr[2];
    // Read serial array 
    Serial.readBytes((char*)arr, 6);
    //Control output  in range 0 - 255)
    analogWrite(BackRight_1, (arr[5]));
    analogWrite(BackLeft_5, (arr[4]));
    analogWrite(FrontLeft_4, (arr[0]));
    analogWrite(Front_3, (arr[2]));  
    analogWrite(FrontRight_2, (arr[1]));
  }
}  
