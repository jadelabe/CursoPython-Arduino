#define pot A0
#define led D2

int val, incomingByte ;
bool parpadeo;

void setup() {
  pinMode(pot, INPUT);
  pinMode(led, OUTPUT);
  
  Serial.begin(9600);
}

void loop() {
  val = analogRead(pot);
Serial.println(val);
  
  incomingByte = Serial.read();
  if(incomingByte == 's'){
    digitalWrite(led, HIGH);
    parpadeo=false;
  } else if (incomingByte == 'a'){
    digitalWrite(led, LOW);
    parpadeo=false;
  }  else if (incomingByte == 'd'){
    parpadeo = true;
  }  else if (incomingByte == 'w'){
     Serial.println(val);
  }

  if(parpadeo){
    digitalWrite(led, HIGH);
    delay(1);
    digitalWrite(led, LOW);
    delay(1);
  }

  delay(100);
}
