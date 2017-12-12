#include <stdio.h>
//#include <stdlib.h>
//#include <time.h>
#include <wiringPi.h>
#include <softPwm.h>

#define A 29	//40
#define B 28	//38
#define C 25	//37
#define D 27	//36
#define E 24	//35
#define F 23	//33
#define G 26	//32
//[common - common] - 3.3V

#define uchar unsigned char

void output(void){
	pinMode(A, OUTPUT);
	pinMode(B, OUTPUT);
	pinMode(C, OUTPUT);
	pinMode(D, OUTPUT);
	pinMode(E, OUTPUT);
	pinMode(F, OUTPUT);
	pinMode(G, OUTPUT);
}


void segInit(void){
	softPwmCreate(A, 0, 1);
	softPwmCreate(B, 0, 1);
	softPwmCreate(C, 0, 1);
	softPwmCreate(D, 0, 1);
	softPwmCreate(E, 0, 1);
	softPwmCreate(F, 0, 1);
	softPwmCreate(G, 0, 1);
}

void setSeg(uchar a, uchar b, uchar c, uchar d, uchar e, uchar f, uchar g){
	softPwmWrite(A, a);
	softPwmWrite(B, b);
	softPwmWrite(C, c);
	softPwmWrite(D, d);
	softPwmWrite(E, e);
	softPwmWrite(F, f);
	softPwmWrite(G, g);
}

void seg0(void){setSeg(0,0,0,0,0,0,1);}

void allHIGH(void){
	digitalWrite(A, HIGH);
	digitalWrite(B, HIGH);
	digitalWrite(C, HIGH);
	digitalWrite(D, HIGH);
	digitalWrite(E, HIGH);
	digitalWrite(F, HIGH);
	digitalWrite(G, HIGH);
}

void allLOW(void){
	digitalWrite(A, LOW);
	digitalWrite(B, LOW);
	digitalWrite(C, LOW);
	digitalWrite(D, LOW);
	digitalWrite(E, LOW);
	digitalWrite(F, LOW);
	digitalWrite(G, LOW);
}

void A_ON(void){digitalWrite(A, LOW);}	//맨위
void B_ON(void){digitalWrite(B, LOW);}	//오른쪽 아래
void C_ON(void){digitalWrite(C, LOW);}	//오른쪽 위
void D_ON(void){digitalWrite(D, LOW);}	//아래
void E_ON(void){digitalWrite(E, LOW);}	//왼쪽 아래
void F_ON(void){digitalWrite(F, LOW);}	//왼쪽 위
void G_ON(void){digitalWrite(G, LOW);}	//가운데

void A_OFF(void){digitalWrite(A, HIGH);}	//맨위
void B_OFF(void){digitalWrite(B, HIGH);}	//오른쪽 아래
void C_OFF(void){digitalWrite(C, HIGH);}	//오른쪽 위
void D_OFF(void){digitalWrite(D, HIGH);}	//아래
void E_OFF(void){digitalWrite(E, HIGH);}	//왼쪽 아래
void F_OFF(void){digitalWrite(F, HIGH);}	//왼쪽 위
void G_OFF(void){digitalWrite(G, HIGH);}	//가운데

void NUM_0(void){allLOW();G_OFF();}
void NUM_1(void){allHIGH();E_ON();F_ON();}
void NUM_2(void){allLOW();F_OFF();B_OFF();}
void NUM_3(void){allLOW();E_OFF();F_OFF();}
void NUM_4(void){allLOW();A_OFF();D_OFF();E_OFF();}
void NUM_5(void){allLOW();C_OFF();E_OFF();}
void NUM_6(void){allLOW();C_OFF();}
void NUM_7(void){allLOW();G_OFF();D_OFF();E_OFF();}
void NUM_8(void){allLOW();}
void NUM_9(void){allLOW();E_OFF();}

int main(void){

	if(wiringPiSetup() == -1){return 1;}
	output();
	
	int num;
	while(1){
		printf("Number Input:");
		scanf("%d", &num);
		if(num == 0){NUM_0();}
		else if(num == 1){NUM_1();}
		else if(num == 2){NUM_2();}
		else if(num == 3){NUM_3();}
		else if(num == 4){NUM_4();}
		else if(num == 5){NUM_5();}
		else if(num == 6){NUM_6();}
		else if(num == 7){NUM_7();}
		else if(num == 8){NUM_8();}
		else if(num == 9){NUM_9();}
		delay(1000);
		printf("turn off\n");
		allHIGH();
		/*
		allHIGH();
		NUM_0();
		delay(1000);
		NUM_1();
		delay(1000);
		NUM_2();
		delay(1000);
		NUM_3();
		delay(1000);
		NUM_4();
		delay(1000);
		NUM_5();
		delay(1000);
		NUM_6();
		delay(1000);
		NUM_7();
		delay(1000);
		NUM_8();
		delay(1000);
		NUM_9();
		delay(1000);
		*/
	}

	return 0;
}
