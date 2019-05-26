#define pot A0
#define led A1
int val;

void setup() {
  pinMode(pot, INPUT);
  pinMode(led, OUTPUT);
  pinMode(6, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  val = analogRead(pot);
  Serial.print(val);
  Serial.println();
  analogWrite(led, val / 4);
  if(val == 1023){
        digitalWrite(6,HIGH);
  }
  else{
        digitalWrite(6,LOW);
  }
  delay(500);
}
