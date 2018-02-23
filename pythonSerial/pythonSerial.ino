const int pulsante = 12;   
const int ledPin = 2; 
int stato;

boolean buttonState = LOW;   
void setup() {

  pinMode(pulsante, INPUT_PULLUP); 
  pinMode(ledPin, OUTPUT);

  Serial.begin(9600); 
}

void loop() {
  buttonState = digitalRead(pulsante);
  

  if (buttonState == LOW) {     

    Serial.println("1");
    
   
for (int i = 0; i <=7; i++) {
      digitalWrite(ledPin, HIGH);   // turn the LED on (HIGH is the voltage level)
      delay(1000);
      digitalWrite(ledPin, LOW);   // turn the LED on (HIGH is the voltage level)
      delay(1000);   
   }      
    
   
  } 

  if(Serial.available()){
    char c = Serial.read();
    if (c == '2') {
      stato='2';
      for (int i = 0; i <= 100; i++) { 
        digitalWrite(ledPin, HIGH);   // turn the LED on (HIGH is the voltage level)
        delay(40);
        digitalWrite(ledPin, LOW);   // turn the LED on (HIGH is the voltage level)
        delay(40);             
      }
    };
  }
  delay(10);

}

