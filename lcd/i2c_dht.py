import smbus
import time
import i2c_module as I2C
import Adafruit_DHT

I2C.lcd_init()  # lcd 초기화

sensor = Adafruit_DHT.DHT11 # DHT version

pin = 4 # BCM 4, WPi 7, pin7

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)
    I2C.lcd_string("{}`C".format(temperature), I2C.LCD_LINE_1)
    I2C.lcd_string("{}%".format(humidity), I2C.LCD_LINE_2)
    time.sleep(1)
