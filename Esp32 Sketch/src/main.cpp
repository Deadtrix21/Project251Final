#include <Arduino.h>

int pinLed {4};
int pinWater {13};


float waterLevel {0};
void setup() {
  Serial.begin(9600);
  pinMode(pinLed, OUTPUT);
  pinMode(23, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  delay(500);
  digitalWrite(pinLed, LOW);
  delay(500);
  digitalWrite(pinLed, HIGH);
  //waterLevel = analogRead(pinWater);
  //Serial.println(waterLevel);
  tone(23, 2000);
  delay(40);
  tone(23, 6000);
  delay(40);
  tone(23, 2000);
  tone(23, 6000);
  delay(40);
  tone(23, 6000);
  delay(40);
  tone(23, 2000);
  Serial.print("Hello world\n");
  

}