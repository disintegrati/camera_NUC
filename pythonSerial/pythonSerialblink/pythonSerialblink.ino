const int pulsante = 10;   
const int ledPin =  13; 
const int blinkled = 12;

boolean buttonState = LOW;   
void setup() {
  
  pinMode(pulsante, INPUT); 
  pinMode(12, OUTPUT);
  Serial.begin(9600); 
}

void loop() {
 buttonState = digitalRead(pulsante);
  
 if (buttonState == LOW) {     
       
    Serial.println("1");
    delay(1000);
    digitalWrite(12, HIGH);
    delay(500);
    digitalWrite(12, LOW);
    delay(500);

  } 
  if (Serial.read() == 2) {
    digitalWrite(ledPin,LOW);
  }
  
  delay(10);
  
}
