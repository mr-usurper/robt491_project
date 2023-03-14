//moving after laser reading

#define enA 9
#define in1 6
#define in2 7

int laser = 2;
int laser2 = 13;
int bluepin = 11; 
int greenpin = 12; 
int redpin = 13; 

int item = 0; 
int thresh1 = 50;
int thresh2 = 50;

void setup() {
  Serial.begin(9600);

  pinMode(enA, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);

  pinMode(laser, OUTPUT); 
  pinMode(laser2, OUTPUT);
  pinMode(A0, INPUT);
  pinMode(A3, INPUT); 
  pinMode(redpin, OUTPUT); 
  pinMode(bluepin, OUTPUT); 
  pinMode(greenpin, OUTPUT); 
 
  digitalWrite(laser, HIGH); 
  digitalWrite(laser2, HIGH);

}

void loop() {

  int value1 = map(analogRead(A3), 0, 1023, 100, 0);
  int value2 = map(analogRead(A0), 0, 1023, 100, 0);

  Serial.println(value2);
  delay(500);

  if (item == 0) {
      if (value1 > thresh1) {
        digitalWrite(in1, LOW);
        digitalWrite(in2, HIGH);
        analogWrite(enA, 0);
        Serial.println("no item");
      } else if (value1 < thresh1) {
        Serial.println("SAW ITEM");
        item = 1;
      }
  } else if (item == 1) {
      if ( value2 > thresh2) {
        digitalWrite(in1, LOW);
        digitalWrite(in2, HIGH);
        analogWrite(enA, 255);
        Serial.println("RUN");
      } else if (value2 < thresh2) {
        Serial.println("DONE DEAL");
        item = 2;
      }
  } else if (item == 2) {
      digitalWrite(in1, LOW);
      digitalWrite(in2, HIGH);
      analogWrite(enA, 0);
      Serial.println("no item");
      
  }

}
