#git clone https://github.com/adafruit/Adafruit_Python_CharLCD.git
#cd ./Adafruit_Python_CharLCD
#sudo python3 setup.py install

import Adafruit_CharLCD as LCD
import time

rs = 21 #pin 40, LCD pin 4
en = 20 #pin 38, LCD pin 6
d4 = 16 #pin 36, LCD pin -6(14)
d5 = 12 #pin 32, LCD pin -5(13)
d6 = 1  #pin 28, LCD pin -4(12)
d7 = 7  #pin 26, LCD pin -3(11)

lcd = LCD.Adafruit_CharLCD(rs, en, d4, d5, d6, d7, 16, 2, 2)

lcd.show_cursor(True)
lcd.message("Show Cursor")
time.sleep(3)
lcd.clear()
lcd.show_cursor(False)

lcd.blink(True)
lcd.message("Blink Cursor")
time.sleep(3)
lcd.clear()
lcd.blink(False)

lcd.message('Scroll')
for i in range(0, 10):
    time.sleep(0.1)
    lcd.move_right()

time.sleep(1)
lcd.clear()
lcd.message("Scroll UpLine\nScroll DownLine")

for i in range(0, 10):
    lcd.move_right()

for i in range(0, 10):
    time.sleep(0.1)
    lcd.move_left()

time.sleep(1)
lcd.clear()

lcd.message("GoodBye!")
time.sleep(3)
lcd.clear()
