#This code uses an ADXL335 acceleromater to measure the speed in the x, y, and z directions.
#The ESP32 utilizes the ADC (Analog to Digital Converter) pins to get data from the accelerometer
#Connect Vcc pin on the sensor to 3.3v pin on the ESP32 (Do not use 5v), Gnd on the sensor to Gnd on the ESP32, x-out on the sensor to GPIO 4 on the ESP32, y-out on the sensor to GPIO 5 on the ESP32, and z-out on the sensor to GPIO 7 on the ESP32
#Reminder, ADXL335 does not work with 5v, use 3.3v instead. Otherwise, the sensor might burn up

from machine import Pin, ADC
from utime import sleep

x=ADC(Pin(4))
y=ADC(Pin(5))
z=ADC(Pin(6))

x.atten(ADC.ATTN_11DB)
y.atten(ADC.ATTN_11DB)
z.atten(ADC.ATTN_11DB)

while True:
    print("X:", x.read(), "Y:", y.read(), "Z:", z.read())
    sleep(0.1)