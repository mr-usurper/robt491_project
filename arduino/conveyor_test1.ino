#define enA 9
#define in1 6
#define in2 7

void setup() {
  Serial.begin(9600);

  pinMode(enA, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
  // Set initial rotation direction
  //digitalWrite(in1, LOW);
  //digitalWrite(in2, HIGH);
}

void loop() {
  //int potValue = 255;
  //int pwmOutput = map(potValue, 0, 1023, 0 , 255); // Map the potentiometer value from 0 to 255
  analogWrite(enA, 255); // Send PWM signal to L298N Enable pin

  //digitalWrite(enA, HIGH);
  if (digitalRead(11) == true) {
    analogWrite(enA, 255);
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
    delay(20);
  } else if (digitalRead(11) == false) {
    analogWrite(enA, 0);
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
    delay(20);
  }
  if (digitalRead(12) == true) {
    analogWrite(enA, 255);
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
    delay(20);
  } else if (digitalRead(12) == false) {
    analogWrite(enA, 0);
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
    delay(20);
  }

  //digitalWrite(in1, HIGH);
  //digitalWrite(in2, LOW);

  

}