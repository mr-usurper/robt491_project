//moving after laser reading

#define enA 9
#define in1 6
#define in2 7
#define laser 2 

int bluepin = 11; // select the pin for the  blue LED 
int greenpin = 12; // select the pin for the green LED 
int redpin = 13; // select the pin for the red LED 
int value = 0; 

void setup() {
  Serial.begin(9600);

  pinMode(enA, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);

  pinMode(laser, OUTPUT); 
  pinMode(A3, INPUT); 
  pinMode(redpin, OUTPUT); 
  pinMode(bluepin, OUTPUT); 
  pinMode(greenpin, OUTPUT); 
 
  digitalWrite(laser, HIGH); 

}

void loop() {

  analogWrite(enA, 255); // Send PWM signal to L298N Enable pin

  value = map(analogRead(A3), 0, 1023, 100, 0);

  if (value < 95) { //move
    analogWrite(enA, 255);
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);

    analogWrite(redpin, 255); 
    analogWrite(greenpin, 0); 

    delay(20);
  } else if (value > 95) {
    analogWrite(enA, 0);
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);

    analogWrite(redpin, 0); 
    analogWrite(greenpin, 255);

    delay(20);
  }
  

}
