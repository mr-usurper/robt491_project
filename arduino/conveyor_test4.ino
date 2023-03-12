//moving after fsr reading

#define enA 9
#define in1 6
#define in2 7

int fsrPin = 0;     // the FSR and 10K pulldown are connected to a0
int fsrReading;     // the analog reading from the FSR resistor divider
String barCode;

void setup() {
  Serial.begin(9600);

  pinMode(enA, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);

  fsrReading = analogRead(fsrPin);

}

void loop() {

  
  //barCode = Serial.readString(); //barcode reader function
  //Serial.print(barCode);

  fsrReading = analogRead(fsrPin);  
 
  Serial.print("Analog reading = ");
  Serial.print(fsrReading);  

  if (fsrReading < 500 && fsrReading > 200) {
    analogWrite(enA, 255); // Send PWM signal to L298N Enable pin
    digitalWrite(in1, LOW);
    digitalWrite(in2, HIGH);
  } else {
    analogWrite(enA, 0); // Send PWM signal to L298N Enable pin
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
  }



  //delay(20);

}