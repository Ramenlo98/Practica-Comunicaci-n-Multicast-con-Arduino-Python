//Creamos una variable de tipo entero para guardar el valor del sensor
int lectura = 0;

void setup() {
  //Iniciamos la comunicación serial
  Serial.begin(9600);
}

void loop() {
  //Tomamos la lectura analógica del pin al cual conectamos
  //la señal de nuestro pequeño circuito divisor de tension
  //y la guardamos en una variable
  lectura = analogRead(0);

  if (lectura <= 450) {
    //Se imprime la N para identifiar que es Noche y debe de encender la luz
    Serial.println("N");
  }
  
  if (lectura >= 460) {
    //Se imprime la N para identifiar que es Noche y debe de encender la luz
    Serial.println("D");
  }
  
  //Imprimimos por monitor serie el valor 
  //Serial.println(lectura);

  delay(1000);
}
