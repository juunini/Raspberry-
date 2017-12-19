import RPi.GPIO as GPIO
from time import sleep

sensor = 11
led = 12
booser = 3

GPIO.setmode(GPIO.BOARD)    #피지컬 넘버로 표기함.
GPIO.setup(sensor, GPIO.IN)
GPIO.setup(led, GPIO.OUT)
GPIO.setup(booser, GPIO.OUT)

try:
    while True: #무한루프
        if GPIO.input(sensor) == True:  #센서 감지
            GPIO.output(led, True)
            GPIO.output(booser, True)
            sleep(0.1)
        else :  #센서 감지 없음
            GPIO.output(led, False)
            GPIO.output(booser, False)
            sleep(0.1)

except KeyboardInterrupt:   #Ctrl+C 로 종료했을 때
    GPIO.cleanup()


GPIO.cleanup()  #끝
