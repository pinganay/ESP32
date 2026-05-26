#Both versions of code below use a BME280 driver from awesome-micropython to detect temp, humidity, and air pressure
#Connect Vcc pin on the BME280 to 3.3v pin on the ESP32 (Do not use 5v) and Gnd on the BME280 to Gnd on the ESP32
#Reminder, BME280 does not work with 5v, use 3.3v instead. Otherwise, the sensor might burn up
#If using hardware I2C, connect SDA pin on BME280 to pin 8 on ESP32 and SCL pin on BME280 to pin 9 on ESP32
#If using software I2C, connect SDA and SCL pins on the BME280 to any of the pairs of pins listed right above the software I2C code



#This code uses the hardware I2C module, which only takes pin 8 for sda and pin 9 for scl

'''
from machine import Pin, I2C
from BME280.bme280_float import *
from utime import sleep


i2c=I2C(0, sda=Pin(8), scl=Pin(9))
print(i2c.scan())
bme280 = BME280(i2c=i2c)
while True:
    print(bme280.values)
    sleep(1)
    
'''

#This code uses the software I2C module, which takes certain pairs of pins for sda and scl
'''
These are the only pairs of pins on the ESP32 that can be used for sda and scl

SoftI2C(sda=Pin(6), scl=Pin(7))
SoftI2C(sda=Pin(4), scl=Pin(5))
SoftI2C(sda=Pin(2), scl=Pin(3))
SoftI2C(sda=Pin(0), scl=Pin(1))
SoftI2C(sda=Pin(20), scl=Pin(21))
'''

from machine import Pin, SoftI2C
from BME280.bme280_float import *
from utime import sleep


i2c=SoftI2C(sda=Pin(6), scl=Pin(7))
print(i2c.scan())

bme280 = BME280(i2c=i2c)
while True:
    print(bme280.values)
    sleep(1)