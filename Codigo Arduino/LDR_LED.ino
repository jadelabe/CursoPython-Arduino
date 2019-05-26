
  int sensorPin = A0; // select the input pin for LDR
  int sensorValue = 0; // variable to store the value coming from the sensor
  int led = D1;
  int incomingByte = 0;
  
void setup() {
Serial.begin(9600); //sets serial port for communication
pinMode(led, OUTPUT);
}

void loop() {
 sensorValue = analogRead(sensorPin); // read the value from the sensor
 Serial.println(sensorValue); //prints the values coming from the sensor on the screen

 if (Serial.available() > 0) {
  incomingByte = Serial.read();
  if(incomingByte == 1){
    digitalWrite(led, HIGH);
  }else if(incomingByte == 0){
    digitalWrite(led, LOW);
  }
  
 }
   // Turn the LED on
  delay(100);
}
