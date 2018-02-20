import smbus
import time
import i2c_module as I2C
import Adafruit_DHT

I2C.lcd_init()  # lcd 초기화

sensor = Adafruit_DHT.DHT11 # DHT version

pin = 4 # BCM 4, WPi 7, pin7

month_string = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
month_num = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

while True:
    humidity, temperature = Adafruit_DHT.read_retry(sensor, pin)

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

    I2C.lcd_string("{}.{}.{}.{}".format(year, month, day, current_time[0:5]), I2C.LCD_LINE_1)
    I2C.lcd_string("{}`C     {}%".format(temperature, humidity), I2C.LCD_LINE_2)
    time.sleep(1)
