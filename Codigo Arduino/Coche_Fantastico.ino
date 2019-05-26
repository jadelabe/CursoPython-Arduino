int pin[6] = {D1, D2, D3, D4, D5, D6};
int tiempo;
void setup() {
  for(int i=0;i<6;i++){
    pinMode(pin[i], OUTPUT);
  }
  pinMode(A0,INPUT);
  Serial.begin(57600);
  
}

void loop() {

  Serial.print(analogRead(A0));
  Serial.println();

  for(int i=0;i<6;i++){
    digitalWrite(pin[i], HIGH);
    delay(analogRead(A0));
    digitalWrite(pin[i], LOW);
  }

   for(int i=5;i>-1;i--){
    digitalWrite(pin[i], HIGH);
    delay(analogRead(A0));
    digitalWrite(pin[i], LOW);
  }
}
