//moving after barcode and fsr reading

#define enA 9
#define in1 6
#define in2 7

int fsrPin = 0;     // the FSR and 10K pulldown are connected to a0
int fsrReading;     // the analog reading from the FSR resistor divider
String barCode;
bool move = LOW;

void setup() {
  Serial.begin(9600);

  pinMode(enA, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);

  fsrReading = analogRead(fsrPin);

}

void loop() {

  barCode = Serial.readString(); //barcode reader function
  Serial.println(barCode);

  //40822426 bottle of water
  //F88D02536NOM parcel

  if(barCode == "F88D02536NOM\n") {
    move = HIGH;
    
  } else if (barCode == "40822426\n") {
    //move = LOW;
    Serial.println("The parcel is not correct");
  }
  Serial.print("MOVE: ");
  Serial.println(move);

  if(move == HIGH) {
    fsrReading = analogRead(fsrPin); 
    Serial.print(fsrReading);

    while(fsrReading < 200) {
       
      analogWrite(enA, 0); // Send PWM signal to L298N Enable pin
      digitalWrite(in1, HIGH);
      digitalWrite(in2, LOW);
      fsrReading = analogRead(fsrPin);
      Serial.println(fsrReading);
      Serial.println("STUCK");
    }
    while(fsrReading < 600 && fsrReading > 200) {
      analogWrite(enA, 255); // Send PWM signal to L298N Enable pin
      digitalWrite(in1, LOW);
      digitalWrite(in2, HIGH);
      fsrReading = analogRead(fsrPin);
      Serial.println(fsrReading);
      Serial.println("im stuck step bro");
    } 
    while(fsrReading < 1000 && fsrReading > 600) {
      analogWrite(enA, 0); // Send PWM signal to L298N Enable pin
      digitalWrite(in1, HIGH);
      digitalWrite(in2, LOW);
      fsrReading = analogRead(fsrPin);
      Serial.println(fsrReading);

      Serial.println("STUCK HEREEEEEEE");

    } 
    move = LOW;
  }

  barCode = "";
  
  //delay(1000);

}


/*
if(move == HIGH) {
    fsrReading = analogRead(fsrPin); 
    if (fsrReading < 500 && fsrReading > 200) {
      analogWrite(enA, 255); // Send PWM signal to L298N Enable pin
      digitalWrite(in1, LOW);
      digitalWrite(in2, HIGH);
    } else {
      analogWrite(enA, 0); // Send PWM signal to L298N Enable pin
      digitalWrite(in1, HIGH);
      digitalWrite(in2, LOW);
    }
    move = LOW;
  }
  */
