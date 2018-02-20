import smbus
import time
import i2c_module as I2C

I2C.lcd_init()  # 초기화

I2C.lcd_string("Hello World", I2C.LCD_LINE_1)       # 윗줄
I2C.lcd_string("Connect Complete", I2C.LCD_LINE_2)  # 아랫줄

time.sleep(3)

I2C.lcd_init()  # 초기화

scroll = "Scroll"   # 스크롤 할 문자
whitespace = " "    # 공백

for i in range(0, 11):
    I2C.lcd_string("{}{}".format(whitespace * i, scroll), I2C.LCD_LINE_1)
    I2C.lcd_string("{}{}".format(whitespace * (10 - i), scroll), I2C.LCD_LINE_2)
    time.sleep(0.01)    # 한계속도. 0.01초로 설정했지만 체감은 0.2 ~ 0.3초

time.sleep(1)
I2C.lcd_init()  # 초기화
