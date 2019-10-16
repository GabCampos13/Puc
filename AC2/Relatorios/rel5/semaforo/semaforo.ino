/*
  Programa 01
  Liga todos os Leds
 */

// Definiçao de valores para variáveis  
int led2 = 2;
int led3 = 3;
int led4 = 4;
int led5 = 5;
int led6 = 6;
int led7 = 7;
int led8 = 8;
int led9 = 9;

int valor1 = 0; //Estado
int pisca = 500;


// Rotina executada 1 vez e que em geral configura entradas e saídas 
void setup() {                
	
	Serial.begin(9600);
	// configura os pinos como saídas DIGITAIS.
	pinMode(led2, OUTPUT);
	pinMode(led3, OUTPUT);
	pinMode(led4, OUTPUT);
	pinMode(led5, OUTPUT);
	pinMode(led6, OUTPUT);
	pinMode(led7, OUTPUT);
	pinMode(led8, OUTPUT);
	pinMode(led9, OUTPUT);
}

// the loop routine runs over and over again forever:
void loop() {

	if(Serial.available() > 0){
  	valor1 = Serial.parseInt();
	
	  //Sinal Pedestre(Verde), Primeiro Sinal(Vermelho), Segundo Sinal(Verde)
    if (valor1 == 1) {
  		digitalWrite(led2, 1);   // Verde(Sinal Pedestre)
  		digitalWrite(led3, 0);   // Vermelho(Sinal Pedestre)
	  	digitalWrite(led4, 0);   // Verde(Primeiro Sinal)	
		  digitalWrite(led5, 0);   // Amarelo(Primeiro Sinal)
  		digitalWrite(led6, 1);   // Vermelho(Primeiro Sinal)
  		digitalWrite(led7, 1);   // Verde(Segundo Sinal)
  		digitalWrite(led8, 0);   // Amarelo(Segundo Sinal)
  		digitalWrite(led9, 0);   // Vermelho(Segundo Sinal)
  	}
	
  	//Sinal Pedestre(Vermelho), Primeiro Sinal(Vermelho), Segundo Sinal(Amarelo)
    if (valor1 == 2) {
  		digitalWrite(led2, 0);   // Verde(Sinal Pedestre)
  		digitalWrite(led3, 1);   // Vermelho(Sinal Pedestre)
  		digitalWrite(led4, 0);   // Verde(Primeiro Sinal)	
  		digitalWrite(led5, 0);   // Amarelo(Primeiro Sinal)
  		digitalWrite(led6, 1);   // Vermelho(Primeiro Sinal)
  		digitalWrite(led7, 0);   // Verde(Segundo Sinal)
  		digitalWrite(led8, 1);   // Amarelo(Segundo Sinal)
  		digitalWrite(led9, 0);   // Vermelho(Segundo Sinal)
      
      //Pisca o Sinal vermelho do pedestre
      delay(pisca);
  	  digitalWrite(led3, 0);   // Vermelho(Sinal Pedestre)
      delay(pisca);
      digitalWrite(led3, 1);   // Vermelho(Sinal Pedestre)
      delay(pisca);
      digitalWrite(led3, 0);   // Vermelho(Sinal Pedestre)
      delay(pisca);
      digitalWrite(led3, 1);   // Vermelho(Sinal Pedestre)
  	}

   
   //Sinal Pedestre(Vermelho), Primeiro Sinal(Verde), Segundo Sinal(Vermelho)
    if (valor1 == 3) {
      digitalWrite(led2, 0);   // Verde(Sinal Pedestre)
      digitalWrite(led3, 1);   // Vermelho(Sinal Pedestre)
      digitalWrite(led4, 1);   // Verde(Primeiro Sinal) 
      digitalWrite(led5, 0);   // Amarelo(Primeiro Sinal)
      digitalWrite(led6, 0);   // Vermelho(Primeiro Sinal)
      digitalWrite(led7, 0);   // Verde(Segundo Sinal)
      digitalWrite(led8, 0);   // Amarelo(Segundo Sinal)
      digitalWrite(led9, 1);   // Vermelho(Segundo Sinal)
    }
  
    //Sinal Pedestre(Vermelho), Primeiro Sinal(Amarelo), Segundo Sinal(Vermelho)
    if (valor1 == 4) {
      digitalWrite(led2, 0);   // Verde(Sinal Pedestre)
      digitalWrite(led3, 1);   // Vermelho(Sinal Pedestre)
      digitalWrite(led4, 0);   // Verde(Primeiro Sinal) 
      digitalWrite(led5, 1);   // Amarelo(Primeiro Sinal)
      digitalWrite(led6, 0);   // Vermelho(Primeiro Sinal)
      digitalWrite(led7, 0);   // Verde(Segundo Sinal)
      digitalWrite(led8, 0);   // Amarelo(Segundo Sinal)
      digitalWrite(led9, 1);   // Vermelho(Segundo Sinal)
    }
	}
}

