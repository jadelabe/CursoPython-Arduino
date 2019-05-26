#include "DHT.h"

#define DHT_PIN D8
#define ATOM D9
#define tierra A0

#define DHTTYPE DHT11
DHT dht(DHT_PIN, DHTTYPE);


void setup(){
  
  pinMode(DHT_PIN,INPUT);
  pinMode(tierra,INPUT);
  pinMode(ATOM,INPUT);
  Serial.begin(57600);
  dht.begin();
}


void loop(){
  float h = dht.readHumidity();
  float t = dht.readTemperature();
  Serial.print("Temperatura:");
  Serial.println(t);
  Serial.print("Humedad:");
  Serial.println(h);
  Serial.print("Tierra:");
  Serial.println(analogRead(tierra));

  digitalWrite(ATOM, HIGH);
  delay(1000);
}
