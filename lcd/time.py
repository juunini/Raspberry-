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

month_string = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
month_num = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

while(True):
    time_split = time.ctime().split(" ")
    year = time_split[4]
    month = time_split[1]
    day = time_split[2]
    week = time_split[0]
    current_time = time_split[3]
    
    for i in range(0, 12):
        if month == month_string[i]:
            month = month_num[i]
            break

    lcd.message("{}.{}.{}.{}\n{}".format(year, month, day, week, current_time))
    time.sleep(1)
    lcd.clear()
