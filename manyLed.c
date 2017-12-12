include <stdio.h>
#include <wiringPi.h>
#include <softPwm.h>

#define LED1 0
#define LED2 1
#define LED3 2
#define LED4 3
#define LED5 4
#define LED6 5
#define LED7 6

void setPin(void){
	pinMode(LED1, OUTPUT);
	pinMode(LED2, OUTPUT);
	pinMode(LED3, OUTPUT);
	pinMode(LED4, OUTPUT);
	pinMode(LED5, OUTPUT);
	pinMode(LED6, OUTPUT);
	pinMode(LED7, OUTPUT);
}

void allDown(void){
	digitalWrite(LED1, LOW);
	digitalWrite(LED2, LOW);
	digitalWrite(LED3, LOW);
	digitalWrite(LED4, LOW);
	digitalWrite(LED5, LOW);
	digitalWrite(LED6, LOW);
	digitalWrite(LED7, LOW);
}

void allUp(void){
	digitalWrite(LED1, HIGH);
	digitalWrite(LED2, HIGH);
	digitalWrite(LED3, HIGH);
	digitalWrite(LED4, HIGH);
	digitalWrite(LED5, HIGH);
	digitalWrite(LED6, HIGH);
	digitalWrite(LED7, HIGH);
}

int main(void){
	if(wiringPiSetup() == -1){return 1;}
	setPin();

	allDown();
	
	int led;
	int result;

	do{
		printf("몇번 핀을 켤까요?");
		result = scanf("%d", &led);

		if(led == 1){digitalWrite(LED1, HIGH);}
		else if(led == 2){digitalWrite(LED2, HIGH);}
		else if(led == 3){digitalWrite(LED3, HIGH);}
		else if(led == 4){digitalWrite(LED4, HIGH);}
		else if(led == 5){digitalWrite(LED5, HIGH);}
		else if(led == 6){digitalWrite(LED6, HIGH);}
		else if(led == 7){digitalWrite(LED7, HIGH);}
		else if(led == 8){allUp();}
		
		delay(3000);
		allDown();
	}while(led != 0);

	return 0;
}

