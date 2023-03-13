#define enA 9
#define in1 6
#define in2 7

void setup() {
  Serial.begin(9600);

  pinMode(enA, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
}

void loop() {
analogWrite(enA, 255); 

  //digitalWrite(enA, HIGH);

  //digitalWrite(in1, LOW);
  //digitalWrite(in2, HIGH);

  digitalWrite(in1, HIGH);
  digitalWrite(in2, LOW);

  //delay(20);

}
