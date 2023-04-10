#include "millisDelay.h"

#define enA 9
#define in1 6
#define in2 7

int laser = 2;
int laser2 = 3;
int bluepin = 11; 
int greenpin = 12; 
int redpin = 13; 
int fsrpin = 1;
int fsr;

int item = 0; 
int thresh1;
int thresh2;
int gogo = 0;

millisDelay pinDelay;

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

  pinDelay.start(1000);

}

void loop() {
  int value1 = map(analogRead(A3), 0, 1023, 100, 0);
  int value2 = map(analogRead(A0), 0, 1023, 100, 0);

  if (gogo == 0) {
    thresh1 = value1 - 20;
    thresh2 = value2 - 20;
  }
  
  if (pinDelay.justFinished()) {
    gogo = 1;
  } else if (gogo == 1) {
    
    if (item == 0) { //no parcel on conveyor
        if (value1 > thresh1) {
          digitalWrite(in1, LOW);
          digitalWrite(in2, HIGH);
          analogWrite(enA, 0);
          analogWrite(redpin, 0);
          analogWrite(greenpin, 255);
          //Serial.println("no item");

          Serial.print("1313");
          
        } else if (value1 < thresh1) {
          //Serial.println("SAW ITEM");
          item = 1;
        }
    } else if (item == 1) { //parcel is on conveyor
        if ( value2 > thresh2) {
          digitalWrite(in1, LOW);
          digitalWrite(in2, HIGH);
          analogWrite(enA, 255);
          analogWrite(redpin, 255);
          analogWrite(greenpin, 0);
          //Serial.println("RUN");

          Serial.print("6969");
          
        } else if (value2 < thresh2) {
          //Serial.println("DONE DEAL");
          item = 2;
        }
    } else if (item == 2) { //parcel is sorted
        digitalWrite(in1, LOW);
        digitalWrite(in2, HIGH);
        analogWrite(enA, 0);
        analogWrite(redpin, 0);
        analogWrite(greenpin, 255);
        //Serial.println("no item");
        Serial.print("7777");
        item = 0;
    }
    fsr = analogRead(fsrpin);
    Serial.print(",");
    Serial.println(fsr);
    
  }
  
  delay(500);
}
