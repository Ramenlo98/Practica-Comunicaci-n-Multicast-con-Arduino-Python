//Pin de salida
const int pinLED = 13;

void setup() 
{
   Serial.begin(9600);
   pinMode(pinLED, OUTPUT);
}
void loop()
{
   if (Serial.available()>0) 
   {
      char option = Serial.read();

      //Si se obtiene un 1 del mensaje de Python, se enciende el led
      if (option == 'N') {
        digitalWrite(pinLED, HIGH);
      }

      //Si se obtiene un 0 del mensaje de Python, se apaga el led
      if (option == 'D') {
        digitalWrite(pinLED, LOW);
      }
   }
}
